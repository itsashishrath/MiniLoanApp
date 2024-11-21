import base64
import magic  # For MIME type detection
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import ValidationError

class BFHLView(APIView):
    def get(self, request):
        # Hardcoded response for GET
        return Response({"operation_code": 1}, status=status.HTTP_200_OK)

    def post(self, request):
        try:
            data = request.data.get("data", [])
            file_b64 = request.data.get("file_b64", None)

            # Extract User Info
            user_id = "john_doe_17091999"
            email = "john@xyz.com"
            roll_number = "ABCD123"

            # Separate numbers and alphabets
            numbers = [item for item in data if item.isdigit()]
            alphabets = [item for item in data if item.isalpha()]

            # Find the highest lowercase alphabet
            lowercase_alphabets = [char for char in alphabets if char.islower()]
            highest_lowercase = max(lowercase_alphabets, default=None)

            # Check for prime numbers
            is_prime_found = any(self.is_prime(int(num)) for num in numbers if num.isdigit())

            # File Validation
            file_valid = False
            file_mime_type = None
            file_size_kb = None
            if file_b64:
                try:
                    decoded_file = base64.b64decode(file_b64)
                    mime_type = magic.from_buffer(decoded_file, mime=True)
                    file_valid = True
                    file_mime_type = mime_type
                    file_size_kb = len(decoded_file) / 1024
                except Exception:
                    file_valid = False

            # Response
            response = {
                "is_success": True,
                "user_id": user_id,
                "email": email,
                "roll_number": roll_number,
                "numbers": numbers,
                "alphabets": alphabets,
                "highest_lowercase_alphabet": [highest_lowercase] if highest_lowercase else [],
                "is_prime_found": is_prime_found,
                "file_valid": file_valid,
                "file_mime_type": file_mime_type,
                "file_size_kb": file_size_kb,
            }
            return Response(response, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"is_success": False, "error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
