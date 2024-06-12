from ai_testing import AiTesting

swagger_path = 'swagger.json'
ai = AiTesting()
swagger_spec = ai.load_swagger(swagger_path)
ai.generate_tests(swagger_spec, "http://localhost:5000")