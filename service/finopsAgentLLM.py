from crewai_tools import ScrapeWebsiteTool
from sentence_transformers import SentenceTransformer
from handlingText import cleanText, normalizeCharacters
from model import finopsPages
from repository import dataCollection

page_links = [
    {"title": "The FinOps Framework Overview", "documentType": "page", "link": 'https://www.finops.org/framework/'},
    {"title": "Principles of FinOps", "documentType": "page", "link": 'https://www.finops.org/framework/principles/'},
    {"title": "Personas in FinOps", "documentType": "page", "link": 'https://www.finops.org/framework/personas/'},
    {"title": "Persona FinOps Practitioner", "documentType": "page", "link": 'https://www.finops.org/framework/persona/finops-practitioner/'},
    {"title": "Persona Leadership", "documentType": "page", "link": 'https://www.finops.org/framework/persona/leadership/'},
    {"title": "Persona Product", "documentType": "page", "link": 'https://www.finops.org/framework/persona/product/'},
    {"title": "Persona Engineering", "documentType": "page", "link": 'https://www.finops.org/framework/persona/engineering/'},
    {"title": "Persona Finance", "documentType": "page", "link": 'https://www.finops.org/framework/persona/finance/'},
    {"title": "Persona Procurement", "documentType": "page", "link": 'https://www.finops.org/framework/persona/procurement/'},
    {"title": "FinOps Phases", "documentType": "page", "link": 'https://www.finops.org/framework/phases/'},
    {"title": "FinOps Maturity Model", "documentType": "page", "link": 'https://www.finops.org/framework/maturity-model/'},
    {"title": "FinOps Domains", "documentType": "page", "link": 'https://www.finops.org/framework/domains/'},
    {"title": "Domain Understand Cloud Usage & Cost", "documentType": "page", "link": 'https://www.finops.org/framework/domains/understand-cloud-usage-cost/'},
    {"title": "Domain Quantify Business Value", "documentType": "page", "link": 'https://www.finops.org/framework/domains/quantify-business-value/'},
    {"title": "Domain Optimize Cloud Usage & Cost", "documentType": "page", "link": 'https://www.finops.org/framework/domains/optimize-cloud-usage-cost/'},
    {"title": "Domain Manage the FinOps Practice", "documentType": "page", "link": 'https://www.finops.org/framework/domains/manage-finops-practice/'},
    {"title": "FinOps Capabilities", "documentType": "page", "link": 'https://www.finops.org/framework/capabilities/'},
    {"title": "Allocation Capability", "documentType": "page", "link": 'https://www.finops.org/framework/capabilities/allocation/'},
    {"title": "Anomaly Management Capability", "documentType": "page", "link": 'https://www.finops.org/framework/capabilities/anomaly-management/'},
    {"title": "Architecting for Cloud Capability", "documentType": "page", "link": 'https://www.finops.org/framework/capabilities/architecting-for-cloud/'},
    {"title": "Benchmarking Capability", "documentType": "page", "link": 'https://www.finops.org/framework/capabilities/benchmarking/'},
    {"title": "Budgeting Capability", "documentType": "page", "link": 'https://www.finops.org/framework/capabilities/budgeting/'},
    {"title": "Cloud Policy & Governance Capability", "documentType": "page", "link": 'https://www.finops.org/framework/capabilities/cloud-policy-governance/'},
    {"title": "Cloud Sustainability Capability", "documentType": "page", "link": 'https://www.finops.org/framework/capabilities/cloud-sustainability/'},
    {"title": "Data Ingestion Capability", "documentType": "page", "link": 'https://www.finops.org/framework/capabilities/data-ingestion/'},
    {"title": "FinOps Assessment Capability", "documentType": "page", "link": 'https://www.finops.org/framework/capabilities/finops-assessment/'},
    {"title": "FinOps Education & Enablement Capability", "documentType": "page", "link": 'https://www.finops.org/framework/capabilities/finops-education-enablement/'},
    {"title": "FinOps Practice Operations Capability", "documentType": "page", "link": 'https://www.finops.org/framework/capabilities/finops-practice-operations/'},
    {"title": "FinOps Tools & Services Capability", "documentType": "page", "link": 'https://www.finops.org/framework/capabilities/finops-tools-services/'},
    {"title": "Forecasting Capability", "documentType": "page", "link": 'https://www.finops.org/framework/capabilities/forecasting/'},
    {"title": "Intersecting Disciplines Capability", "documentType": "page", "link": 'https://www.finops.org/framework/capabilities/intersecting-disciplines/'},
    {"title": "Invoicing & Chargeback Capability", "documentType": "page", "link": 'https://www.finops.org/framework/capabilities/invoicing-chargeback/'},
    {"title": "Licensing & SaaS Capability", "documentType": "page", "link": 'https://www.finops.org/framework/capabilities/licensing-saas/'},
    {"title": "Onboarding Workloads Capability", "documentType": "page", "link": 'https://www.finops.org/framework/capabilities/onboarding-workloads/'},
    {"title": "Planning & Estimating Capability", "documentType": "page", "link": 'https://www.finops.org/framework/capabilities/planning-estimating/'},
    {"title": "Rate Optimization Capability", "documentType": "page", "link": 'https://www.finops.org/framework/capabilities/rate-optimization/'},
    {"title": "Reporting & Analytics Capability", "documentType": "page", "link": 'https://www.finops.org/framework/capabilities/reporting-analytics/'},
    {"title": "Unit Economics Capability", "documentType": "page", "link": 'https://www.finops.org/framework/capabilities/unit-economics/'},
    {"title": "Workload Optimization Capability", "documentType": "page", "link": 'https://www.finops.org/framework/capabilities/workload-optimization/'},
    {"title": "FinOps Scope", "documentType": "page", "link": 'https://www.finops.org/framework/scopes/'},
]

# Modelo de Aprendizado de máquina utilizado no embeddings da base de dados.
model = SentenceTransformer('all-MiniLM-L6-v2')

file_path = 'extracted_content_finops.txt'
consolidatedContent = ""
id = 0

with open(file_path, 'w', encoding='utf-8') as file:
    for page in page_links:
        title = page["title"]
        link = page["link"]
        documentType = page["documentType"]
        id = id + 1
        uniqueID = id

        print(f"Extraindo o conteúdo da página: {link}")
        
        tool = ScrapeWebsiteTool(website_url=link)
        try:
            text = tool.run()
        except Exception as e:
            print(f"Erro ao extrair conteúdo de {link}: {e}")
            continue
        
        collection = finopsPages.create_or_get_collection()

        handlingText = cleanText(text)
        normalizedText = normalizeCharacters(handlingText)
        textEmbedding = model.encode([normalizedText])[0]

        originalText = normalizedText
        if len(originalText) > 65000:
            originalText = "Conteudo da Página e Muito Grande Para Vizualizar o Texto Original"

        dataCollection.createDataCollection(collection, title, link, originalText, documentType, textEmbedding, uniqueID)
        consolidatedContent += f"\n\n{title}\n{normalizedText}"

        file.write(f"{title}\n")
        file.write(f"Conteúdo da página: {link}\n")
        file.write(normalizedText)
        file.write("\n\n")

    id = id + 1
    uniqueID = id
    print(f'Identificador unico gerado: {uniqueID}')

    textEmbedding = model.encode([consolidatedContent])[0]
    dataCollection.createDataCollection(collection, "FinOps Consolidated Content", "https://www.finops.org/", "Conteudo Consolidadoe Muito Grande Para Vizualizar o Texto Original", "Consolidated Content", textEmbedding, uniqueID)

print(f'Todo o conteúdo foi gravado no arquivo {file_path}')