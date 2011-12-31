from django.db import models
from django.template.defaultfilters import slugify

from util.html import clean_html

import re
import yaml


class Exercise(models.Model):
    """An exercise for a student to ponder."""
    # The short url-able name for the exercise.
    slug = models.CharField(max_length=80, db_index=True)
    # The human-readable name for the exercise.
    name = models.CharField(max_length=80)
    # The HTML text of the problem, for the student to read.
    text = models.TextField()
    # The Python code to check the student's answer.
    check = models.TextField()
    # A solution to the exercise.  This is used for testing the exercise.
    # Maybe we'll also make it available to the student?
    solution = models.TextField()

    def __unicode__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return ('gym_show_exercise', [str(self.id), slugify(self.name)])

    @classmethod
    def from_yaml(cls, yaml_file):
        """Create an Exercise from a YAML file."""
        data = yaml.load(yaml_file)
        ex, new = cls.objects.get_or_create(slug=data['slug'])
        ex.name = data['name']
        ex.text = clean_html(data['text'])
        ex.check = data['check']
        ex.solution = data.get('solution', '')
        return ex

    def as_yaml(self):
        """Return a YAML string representing this exercise."""
        return yaml.dump(mapping([
            ("slug", quoted(self.slug)),
            ("name", quoted(self.name)),
            ("text", literal(self.text)),
            ("check", literal(self.check)),
            ("solution", literal(self.solution)),
            ]), indent=4)

# Configure PyYaml

class quoted(str): pass
class literal(str): pass
class mapping(list): pass

yaml.add_representer(quoted,
    lambda dumper, data: dumper.represent_scalar('tag:yaml.org,2002:str', data, style='"')
    )

yaml.add_representer(literal, 
    # PyYaml won't use literal blocks if there's trailing space, so trim trailing space from the data.
    lambda dumper, data: dumper.represent_scalar('tag:yaml.org,2002:str', re.sub(r"\s+\n", "\n", data), style='|')
    )

yaml.add_representer(mapping, 
    lambda dumper, data: dumper.represent_dict(data)
    )
