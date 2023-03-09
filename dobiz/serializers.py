from rest_framework import serializers
from .models import *

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class MeaningSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meaning
        fields = '__all__'

class MinimumRequirementSerializer(serializers.ModelSerializer):
    class Meta:
        model = MinimumRequirement
        fields = '__all__'

class BenefitsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Benefits
        fields = '__all__'

class DocumentRequiredSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentRequired
        fields = '__all__'

class IncorporationProcessSerializer(serializers.ModelSerializer):
    class Meta:
        model = IncorporationProcess
        fields = '__all__'

class ComplianceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Compliance
        fields = '__all__'

class StepWiseProcedureSerializer(serializers.ModelSerializer):
    class Meta:
        model = StepWiseProcedure
        fields = '__all__'

class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = '__all__'
        
class PricingSumSerializer(serializers.ModelSerializer):
    class Meta:
        model = PricingSum
        fields = '__all__'

class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = '__all__'

class ClosureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Closure
        fields = '__all__'

class ContactUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields= '__all__'