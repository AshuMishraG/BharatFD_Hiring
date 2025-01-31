from django.db import models
from ckeditor.fields import RichTextField

class FAQ(models.Model):
    question = models.TextField()
    answer = RichTextField()
    question_hi = models.TextField(blank=True, null=True)
    answer_hi = RichTextField(blank=True, null=True)
    question_bn = models.TextField(blank=True, null=True)
    answer_bn = RichTextField(blank=True, null=True)

    def get_translation(self, lang):
        if lang == 'hi':
            return self.question_hi or self.question, self.answer_hi or self.answer
        elif lang == 'bn':
            return self.question_bn or self.question, self.answer_bn or self.answer
        return self.question, self.answer

    def __str__(self):
        return self.question