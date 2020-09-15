from django.db import models


class Endpoint(models.Model):
    """
    The endpoint object represents ML API endpoint.

    Attributes:
        (string) name: The name of the endpoint, it will be used in API URL
        (string) owner: The string with owner name
        (datetime) created_at: The date when endpoint was created.
    """

    name = models.CharField(max_length=128)
    owner = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now=True, blank=True)


class MLAlgorithm(models.Model):
    """
    The MLAlgorithm represents the ML algorithm object.

    Attributes:
        (string) name: Name of the algorithm
        (string) description: Short description of how it works
        (string) code: The code of the algorithm
        (string) version: The version of the algorithm being used
        (string) owner:The name of the owner
        (datetime) created_at: the date when MLAlgorithm was added.
        (FK) parent_endpoint: The reference to the Endpoint
    """
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=1000)
    code = models.CharField(max_length=50000)
    version = models.CharField(max_length=128)
    owner = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    parent_endpoint = models.ForeignKey(Endpoint, on_delete=models.CASCADE)


class MLAlgorithmStatus(models.Model):
    """
    The MLAlgorithmStatus represents status of the MLAgorithm

    Attributes:
        (string) status: The status of algorithm used for the endpoint. Can be: testing, staging, production, ab_testing
        (string) active: The boolean flag which points to currently
        (string) create_by: Name of creator of status.
        (datetime) created_at: The date of status creation.
        (FK) parent_mlalgorithm: The reference to corresponding MLAlgorithm
    """
    status = models.CharField(max_length=128)
    active = models.BooleanField()
    created_by = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    parent_mlalgorithm = models.ForeignKey(MLAlgorithm, on_delete=models.CASCADE, related_name="status")


class MLRequest(models.Model):
    """
    The MLRequest will keep information about all requests to ML algorithms.

    Attributes:
        (string) input_data: The input data to ML Algorithm in JSON format.
        (string)full_response: The response of the ML Algorithm.
        (string)response: The response of the ML algorithm in JSON format
        (string)feedback: The feedback about the response in JSON format.
        (datetime) created_at: The date when request was created.
        (FK) parent_mlalgorithm: The reference to MLAlgorithm used to compute response
    """
    input_data = models.CharField(max_length=10000)
    full_response = models.CharField(max_length=10000)
    response = models.CharField(max_length=10000)
    feedback = models.CharField(max_length=10000, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    parent_mlalgorithm = models.ForeignKey(MLAlgorithm, on_delete=models.CASCADE)
