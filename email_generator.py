# email_generator.py
import openai

def generate_email(email_context, products, company_name, api_key):
    """
    Generate personalized outreach email using AI.
    
    Args:
        email_context (str): Context about the prospect and email purpose
        products (str): Products/services description
        company_name (str): Sender's company name
        api_key (str): OpenAI API key
        
    Returns:
        str: Personalized email content
    """
    if not api_key:
        return "❌ OpenAI API key is required"
    
    if not api_key.startswith('sk-'):
        return "❌ Invalid API key format"
    
    try:
        openai.api_key = api_key
        
        prompt = f"""
        Escribe un email de outreach altamente personalizado para ventas B2B:

        CONTEXTO DEL EMAIL:
        {email_context}

        MI OFERTA:
        {products}

        MI EMPRESA:
        {company_name}

        Requisitos del email:
        - Máximo 150 palabras
        - Tono profesional pero cercano
        - Personalizado con datos específicos del prospecto
        - Value proposition clara
        - Llamado a acción específico
        - Asunto persuasivo (incluir asunto separado)

        Formato:
        ASUNTO: [asunto aquí]

        [cuerpo del email]
        """
        
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Eres un copywriter experto en emails de ventas B2B con altas tasas de respuesta."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=800,
            temperature=0.8
        )
        
        return response.choices[0].message.content
        
    except openai.error.AuthenticationError:
        return "❌ Authentication failed. Please check your API key."
    except openai.error.RateLimitError:
        return "❌ Rate limit exceeded. Please try again later."
    except Exception as e:
        return f"❌ Error generating email: {str(e)}"