# ai-create-testing

## Sobre:
Projeto apresentado no TDC Florianópolis em 2024 para mostrar como podemos utilizar a API do OpenAI.

Neste caso estamos gerando os testes de API automaticamente passando o swagger do nosso serviço. O projeto do server é feito em python, o script para geração dos testes tb está em python e os testes criados estão em pytest.

- Para subir o server:
'''
python .\tdc\app.py
'''
- Para executar a criação dos testes pelo OpenAI:
'''
python .\tdc\ai\create_tests.py
'''
- Para executar os testes
'''
pytest .\tests\test_customer.py
'''

## Links

- Token: https://platform.openai.com/api-keys
- Crédito: https://platform.openai.com/usage
- Storage: https://platform.openai.com/storage
- Billing: https://platform.openai.com/settings/organization/billing/overview
- Tokenizer: https://platform.openai.com/tokenizer
- Price: https://openai.com/api/pricing/