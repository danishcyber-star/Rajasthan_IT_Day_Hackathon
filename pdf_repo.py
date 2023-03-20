from fpdf import FPDF


class PDFReport(FPDF):
    def __init__(self, summary):
        super().__init__()
        self.summary = summary

    def build_report(self):
        self.add_page()
        self.add_font('NotoSans', '', 'NotoSans-Regular.ttf', uni=True)
        self.set_font('NotoSans', '', 12)
        self.cell(0, 10, 'Summary Report / सारांश रिपोर्ट', 0, 1, 'C')
        self.ln(20)
        if isinstance(self.summary, str):
            self.multi_cell(0, 10, self.summary)
        else:
            self.multi_cell(0, 10, self.summary.decode('utf-8'))

   
