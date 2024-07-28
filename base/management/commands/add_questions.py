# appname/management/commands/add_questions.py
from django.core.management.base import BaseCommand
from base.models import Quiz, Question

class Command(BaseCommand):
    help = 'Add more related questions to the specified quiz'

    def handle(self, *args, **kwargs):
        quiz, created = Quiz.objects.get_or_create(
            title='Mental Health Quiz',
            defaults={'description': 'A self-assessment quiz for monitoring mental health.'}
        )

        questions = [
            {
                'text': 'How often have you been bothered by feeling down, depressed, or hopeless?',
                'option1': 'Not at all',
                'option2': 'Several days',
                'option3': 'More than half the days',
                'option4': 'Nearly every day',
                'correct_option': 'Not at all'
            },
            {
                'text': 'How often have you been bothered by little interest or pleasure in doing things?',
                'option1': 'Not at all',
                'option2': 'Several days',
                'option3': 'More than half the days',
                'option4': 'Nearly every day',
                'correct_option': 'Not at all'
            },
            {
                'text': 'How often have you been bothered by trouble falling or staying asleep, or sleeping too much?',
                'option1': 'Not at all',
                'option2': 'Several days',
                'option3': 'More than half the days',
                'option4': 'Nearly every day',
                'correct_option': 'Not at all'
            },
            {
                'text': 'How often have you been bothered by feeling tired or having little energy?',
                'option1': 'Not at all',
                'option2': 'Several days',
                'option3': 'More than half the days',
                'option4': 'Nearly every day',
                'correct_option': 'Not at all'
            },
            {
                'text': 'How often have you been bothered by poor appetite or overeating?',
                'option1': 'Not at all',
                'option2': 'Several days',
                'option3': 'More than half the days',
                'option4': 'Nearly every day',
                'correct_option': 'Not at all'
            },
            {
                'text': 'How often have you been bothered by feeling bad about yourself, or that you are a failure or have let yourself or your family down?',
                'option1': 'Not at all',
                'option2': 'Several days',
                'option3': 'More than half the days',
                'option4': 'Nearly every day',
                'correct_option': 'Not at all'
            },
            {
                'text': 'How often have you been bothered by trouble concentrating on things, such as reading the newspaper or watching television?',
                'option1': 'Not at all',
                'option2': 'Several days',
                'option3': 'More than half the days',
                'option4': 'Nearly every day',
                'correct_option': 'Not at all'
            },
            {
                'text': 'How often have you been bothered by moving or speaking so slowly that other people could have noticed? Or the opposite — being so fidgety or restless that you have been moving around a lot more than usual?',
                'option1': 'Not at all',
                'option2': 'Several days',
                'option3': 'More than half the days',
                'option4': 'Nearly every day',
                'correct_option': 'Not at all'
            },
            {
                'text': 'How often have you been bothered by thoughts that you would be better off dead or of hurting yourself in some way?',
                'option1': 'Not at all',
                'option2': 'Several days',
                'option3': 'More than half the days',
                'option4': 'Nearly every day',
                'correct_option': 'Not at all'
            },
            {
                'text': 'If you checked off any problems, how difficult have these problems made it for you to do your work, take care of things at home, or get along with other people?',
                'option1': 'Not difficult at all',
                'option2': 'Somewhat difficult',
                'option3': 'Very difficult',
                'option4': 'Extremely difficult',
                'correct_option': 'Not difficult at all'
            }
        ]

        for question_data in questions:
            Question.objects.get_or_create(
                quiz=quiz,
                text=question_data['text'],
                defaults={
                    'option1': question_data['option1'],
                    'option2': question_data['option2'],
                    'option3': question_data['option3'],
                    'option4': question_data['option4'],
                    'correct_option': question_data['correct_option']
                }
            )

        self.stdout.write(self.style.SUCCESS('Successfully added more related questions to the quiz'))
