# ai_analyzer.py
import openai
import streamlit as st

def analyze_prospect(prospect_data, products, company_context, api_key):
    """
    Analyze prospect data and generate comprehensive sales strategy using AI.
    
    Args:
        prospect_data (str): Formatted string with prospect information
        products (str): Description of products/services offered
        company_context (str): Information about the seller's company
        api_key (str): OpenAI API key
        
    Returns:
        str: AI-generated sales strategy and analysis
    """
    if not api_key:
        return "❌ OpenAI API key is required"
    
    # Validar que la API key tenga formato correcto
    if not api_key.startswith('sk-'):
        return "❌ Invalid API key format"
    
    try:
        openai.api_key = api_key
        
        prompt = f"""
        Eres un experto en ventas B2B con 15 años de experiencia. Analiza este prospecto y genera una estrategia completa:

        INFORMACIÓN DEL PROSPECTO:
        {prospect_data}

        MI OFERTA COMERCIAL:
        {products}

        CONTEXTO DE MI EMPRESA:
        {company_context}

        Genera un reporte estructurado con:

        🎯 **ANÁLISIS DEL PERFIL**
        - Fit potencial con nuestra oferta (1-10)
        - Pain points detectados basados en su perfil
        - Oportunidades de valor específicas

        💡 **ESTRATEGIA DE VENTA**
        - 3 argumentos de venta personalizados
        - 2 objeciones previsibles y respuestas
        - Ángulo de aproximación recomendado

        📞 **PLAN DE ACCIÓN**
        - Mejor momento para contactar
        - Canal recomendado (email, llamada, LinkedIn)
        - Mensaje inicial personalizado
        - Preguntas clave para descubrir necesidades

        ⚠️ **ALERTAS Y RIESGOS**
        - Posibles desafíos en la venta
        - Factores competitivos a considerar

        Formato: Claro, accionable y listo para usar por el equipo de ventas.
        """
        
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Eres el mejor estratega de ventas B2B del mundo. Tu análisis transforma datos en oportunidades concretas."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=1500,
            temperature=0.7
        )
        
        return response.choices[0].message.content
        
    except openai.error.AuthenticationError:
        return "❌ Authentication failed. Please check your API key."
    except openai.error.RateLimitError:
        return "❌ Rate limit exceeded. Please try again later."
    except openai.error.APIError as e:
        return f"❌ OpenAI API error: {str(e)}"
    except Exception as e:
        return f"❌ Error in AI analysis: {str(e)}"

def quick_analyze(quick_info, products, api_key):
    """
    Quick analysis with minimal prospect information.
    
    Args:
        quick_info (str): Brief description of the prospect
        products (str): Products/services offered
        api_key (str): OpenAI API key
        
    Returns:
        str: Quick strategic insights
    """
    if not api_key:
        return "❌ OpenAI API key is required"
    
    if not api_key.startswith('sk-'):
        return "❌ Invalid API key format"
    
    try:
        openai.api_key = api_key
        
        prompt = f"""
        Basado en esta información limitada, genera insights rápidos de venta:

        INFORMACIÓN RÁPIDA: {quick_info}
        OFERTA: {products}

        Proporciona:
        - 2 oportunidades principales
        - 1 ángulo de aproximación
        - 1 pregunta descubridora clave

        Máximo 300 palabras.
        """
        
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Eres un experto en ventas que puede generar insights rápidos con poca información."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=500,
            temperature=0.8
        )
        
        return response.choices[0].message.content
        
    except Exception as e:
        return f"❌ Error in quick analysis: {str(e)}"