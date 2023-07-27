```python
class CodeTemplates:
    def __init__(self):
        self.templates = {
            "python": {
                "file": "# Python file\n\n",
                "function": "def function_name():\n    pass\n",
                "class": "class ClassName:\n    pass\n"
            },
            "javascript": {
                "file": "// JavaScript file\n\n",
                "function": "function functionName() {\n}\n",
                "class": "class ClassName {\n}\n"
            },
            "java": {
                "file": "// Java file\n\n",
                "function": "public void functionName() {\n}\n",
                "class": "public class ClassName {\n}\n"
            }
        }

    def get_template(self, language, template_type):
        if language in self.templates and template_type in self.templates[language]:
            return self.templates[language][template_type]
        else:
            return None
```