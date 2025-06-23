import json
import markdown2
from fpdf import FPDF
from datetime import datetime
import os

def get_current_date_in_english():
    now = datetime.now()
    return now.strftime("%B %d, %Y")

class PDF(FPDF):
    def footer(self):
        self.set_y(-15)
        try:
            self.set_font("Lato", "I", 8)
        except RuntimeError:
            self.set_font("Arial", "I", 8)
        self.cell(0, 10, f"Page {self.page_no()}/{{nb}}", 0, 0, "C")

def create_professional_pdf(title: str, description: str, report_markdown: str) -> dict:
    try:
        file_name = "report.pdf"
        static_dir = "static"
        os.makedirs(static_dir, exist_ok=True)
        output_path = os.path.join(static_dir, file_name)
        download_url = f"/static/{file_name}"

        pdf = PDF()
        pdf.set_auto_page_break(auto=True, margin=25)
        pdf.alias_nb_pages()

        try:
            ruta_base_fuentes = "coordinator/sub_agents/pdf_generator/fonts/"
            pdf.add_font("Lato", "", f"{ruta_base_fuentes}Lato-Regular.ttf")
            pdf.add_font("Lato", "B", f"{ruta_base_fuentes}Lato-Bold.ttf")
            pdf.add_font("Lato", "I", f"{ruta_base_fuentes}Lato-Italic.ttf")
            active_font = "Lato"
        except RuntimeError:
            print("WARNING: Lato fonts not found. Using 'Arial' as default.")
            active_font = "Arial"

        pdf.add_page()
        pdf.set_font(active_font, "B", 36)
        pdf.multi_cell(0, 20, title, 0, "C")
        pdf.ln(15)
        pdf.set_font(active_font, "I", 16)
        pdf.multi_cell(0, 10, description, 0, "C")
        pdf.set_y(250)
        pdf.set_font(active_font, "", 12)
        pdf.cell(0, 10, get_current_date_in_english(), 0, 0, "C")

        raw_sections = report_markdown.split('## ')
        sections = {}
        for sec in raw_sections:
            if not sec.strip():
                continue
            parts = sec.split('\n', 1)
            title_line = parts[0].strip()
            content = parts[1].strip() if len(parts) > 1 else ""
            sections[title_line] = content
        
        order = list(sections.keys())

        for section_title in order:
            content_raw = sections[section_title].strip().rstrip('#').strip()
            
            pdf.add_page()
            pdf.set_font(active_font, "B", 20)
            pdf.set_text_color(0, 0, 0)
            pdf.multi_cell(0, 10, section_title, 0, "L")
            pdf.ln(5)

            pdf.set_font(active_font, "", 12)
            pdf.set_text_color(50, 50, 50)
            
            if "Table of Contents" in section_title or "References" in section_title:
                items = content_raw.split('\n')
                for item in items:
                    item_clean = item.strip().lstrip('*').strip()
                    if item_clean:
                        pdf.multi_cell(0, 7, f"•  {item_clean}")
                        pdf.ln(2)
            else:
                section_html = markdown2.markdown(content_raw, extras=["cuddled-lists", "tables", "fenced-code-blocks"])
                pdf.write_html(section_html)

        pdf.output(output_path)
        return {"status": "success", "path": output_path, "download_url": download_url}

    except Exception as e:
        print(f"Error in create_professional_pdf: {e}")
        return {"status": "error", "message": str(e)}