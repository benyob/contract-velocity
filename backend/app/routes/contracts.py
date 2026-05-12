from fastapi import APIRouter, UploadFile, File
from app.services.parser_service import parse_document
from app.services.classifier_service import classify_contract
from app.services.clause_extractor import extract_clauses
from app.services.template_comparator import compare_against_template
from app.services.retrieval_service import retrieve_similar_cases
from app.services.llm_service import analyze_contract
from app.services.routing_service import route_contract

router = APIRouter(prefix="/contracts", tags=["contracts"])

@router.post("/analyze")
async def analyze_contract_endpoint(file: UploadFile = File(...)):

    text = await parse_document(file)

    contract_type = classify_contract(text)

    clauses = extract_clauses(text)

    deviations = compare_against_template(contract_type, clauses)

    precedents = retrieve_similar_cases(deviations)

    ai_analysis = analyze_contract(
        text=text,
        clauses=clauses,
        deviations=deviations,
        precedents=precedents
    )

    routing = route_contract(ai_analysis)

    return {
        "contract_type": contract_type,
        "clauses": clauses,
        "deviations": deviations,
        "precedents": precedents,
        "analysis": ai_analysis,
        "routing": routing
    }