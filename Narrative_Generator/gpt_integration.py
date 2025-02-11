from openai import OpenAI
import jinja2

class ReportWriter:
    def __init__(self):
        self.client = OpenAI(api_key="your_key")
        self.template_loader = jinja2.FileSystemLoader('./prompt_templates')
        
    def generate_report(self, df):
        analysis = {
            'total_items': len(df),
            'critical_items': df[df['status'] == 'Critical'].shape[0],
            'most_stocked': df['item_name'].value_counts().idxmax()
        }
        
        prompt_template = self.template_loader.get_template('executive_summary.j2')
        prompt = prompt_template.render(data=analysis)
        
        response = self.client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}]
        )
        
        return response.choices[0].message.content
