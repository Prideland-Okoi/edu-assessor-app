from rest_framework import serializers
from newtest.models import Assessment, Question, Choice
from rest_framework.exceptions import ValidationError


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ['id', 'choice_text', 'is_correct']

class ChoiceWithOutAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ['choice_text'] #'id'

class QuestionSerializer(serializers.ModelSerializer):
    choices = ChoiceWithOutAnswerSerializer(many=True)

    class Meta:
        model = Question
        fields = ['question_text', 'assessment', 'choices'] # 'id', 'created_at', 'updated_at',
    
    def validate(self, data):
        question_text = data.get('question_text')
        assessment_id = data.get('assessment')
        choices = data.get('choices', [])

        if not question_text:
            raise serializers.ValidationError("Question text is required.")
        # if assessment_id is not None:
        #     try:
        #         assessment = Assessment.objects.get(pk=assessment_id)
        #     except Assessment.DoesNotExist:
        #         raise serializers.ValidationError(f"Assessment with ID {assessment_id} does not exist.")
        if not choices:
            raise serializers.ValidationError("At least one choice is required for a question.")

        return data
        
    def create(self, validated_data):
        choices_data = validated_data.pop('choices', [])  # Use an empty list as a default if 'choices' is not present

        question = Question.objects.create(**validated_data)

        for choice_data in choices_data:
            Choice.objects.create(question=question, **choice_data)

        return question



# class ChoiceSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Choice
#         fields = '__all__'

# class QuestionSerializer(serializers.ModelSerializer):
#     choices = ChoiceSerializer(many=True, read_only=True)

#     class Meta:
#         model = Question
#         fields = '__all__'

class AssessmentSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Assessment
        fields = ("id", "title", "description", "created_at", "questions")
        
    def validate(self, data):
        title = data.get("title")
        description = data.get("description")

        if not title:
            raise ValidationError("Title is required.")

        if not description:
            raise ValidationError("Description is required.")

        return data

