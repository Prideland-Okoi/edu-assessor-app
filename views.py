from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from newtest.models import Assessment, Question
from newtest.serializers import AssessmentSerializer, QuestionSerializer
from rest_framework import generics
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
# Create your views here.


class AssessmentViewSet(viewsets.ModelViewSet):
    queryset = Assessment.objects.all()
    serializer_class = AssessmentSerializer

    def create(self, request, *args, **kwargs):
        # Deserialize the request data using the AssessmentSerializer
        serializer = self.get_serializer(data=request.data)
        
        if serializer.is_valid():
            # Save the assessment to the database
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def list(self, request, *args, **kwargs):
        assessments = self.get_queryset()
        
        if not assessments.exists():
            # Customize the response when no assessments are available
            return Response({'message': 'No assessments created yet.'}, status=status.HTTP_200_OK)
        
        serializer = self.get_serializer(assessments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    def create(self, request, *args, **kwargs):
        # Deserialize the request data using the AssessmentSerializer
        serializer = self.get_serializer(data=request.data)
        
        if serializer.is_valid():
            # Save the assessment to the database
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def list(self, request, *args, **kwargs):
        questions = self.get_queryset()
        
        if not questions.exists():
            # Customize the response when no assessments are available
            return Response({'message': 'No question created for this assessment.'}, status=status.HTTP_200_OK)
        
        serializer = self.get_serializer(questions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)



class QuestionCreateView(generics.CreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    def create(self, request, *args, **kwargs):
        # Deserialize the request data using the QuestionSerializer
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Save the question to the database
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AssessmentCreateView(generics.CreateAPIView):
    queryset = Assessment.objects.all()
    serializer_class = AssessmentSerializer

    def create(self, request, *args, **kwargs):
        # Deserialize the request data using the AssessmentSerializer
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Save the assessment to the database
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


