from fpdf import FPDF

# class PDFReport(FPDF):
#     def __init__(self, summary):
#         super().__init__()
#         self.summary = summary
#
#     # def build_report(self):
#     #     self.add_page()
#     #     self.set_font('Arial', 'B', 16)
#     #     self.cell(0, 10, 'Summary Report', 0, 1, 'C')
#     #     self.ln(20)
#     #     self.set_font('Arial', '', 12)
#     #     self.multi_cell(0, 10, self.summary)


# class PDFReport(FPDF):
    # def __init__(self, summary):
    #     super().__init__()
    #     self.summary = summary
    #
    # def build_report(self):
    #     self.add_page()
    #     self.add_font('DejaVu', '', 'DejaVuSans.ttf', uni=True)
    #     self.set_font('DejaVu', '', 12)
    #     self.cell(0, 10, 'सारांश रिपोर्ट', 0, 1, 'C')
    #     self.ln(20)
    #     self.multi_cell(0, 10, self.summary.encode('utf-8'))


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

    # def build_report(self):
    #     self.add_page()
    #     self.add_font('NotoSans', '', 'NotoSans-Regular.ttf', uni=True)
    #     self.add_font('HindiFont', '', 'Mangal.ttf', uni=True) # added Hindi font
    #     self.set_font('NotoSans', '', 12)
    #     self.cell(0, 10, 'Summary Report / सारांश रिपोर्ट', 0, 1, 'C')
    #     self.ln(20)
    #     if isinstance(self.summary, str):
    #         self.multi_cell(0, 10, self.summary)
    #     else:
    #         self.set_font('HindiFont', '', 14) # increased font size for Hindi text
    #         self.multi_cell(0, 10, self.summary) # removed 'decode' call

    # def build_report(self):
    #     self.add_page()
    #     self.add_font('NotoSans', '', 'NotoSans-Regular.ttf', uni=True)
    #     self.add_font('NotoSansDevanagari', '', 'NotoSansDevanagari-Regular.ttf', uni=True)
    #     self.set_font('NotoSans', '', 12)
    #     self.cell(0, 10, 'Summary Report / सारांश रिपोर्ट', 0, 1, 'C')
    #     self.ln(20)
    #     if isinstance(self.summary, str):
    #         self.multi_cell(0, 10, self.summary)
    #     else:
    #         self.set_font('NotoSansDevanagari', '', 14)
    #         self.multi_cell(0, 10, self.summary)
        # self.add_page()
        # self.add_font('NotoSans', '', 'NotoSans-Regular.ttf', uni=True)
        # self.add_font('NotoSansDevanagari', '', 'NotoSansDevanagari-Regular.ttf', uni=True)  # added Devanagari font
        # self.set_font('NotoSans', '', 12)
        # self.cell(0, 10, 'Summary Report / सारांश रिपोर्ट', 0, 1, 'C')
        # self.ln(20)
        # if isinstance(self.summary, str):
        #     self.set_font('NotoSansDevanagari', '', 14)  # set font for Hindi text
        #     self.multi_cell(0, 10, self.summary)
        # else:
        #     self.multi_cell(0, 10, self.summary)

# class PDFReport(FPDF):
#     def __init__(self, summary):
#         super().__init__()
#         self.summary = summary
#
#         def build_report(self):
#         self.add_page()
#         self.add_font('NotoSans', '', 'NotoSans-Regular.ttf', uni=True)
#         self.add_font('HindiFont', '', 'Mangal.ttf', uni=True) # added Hindi font
#         self.set_font('NotoSans', '', 12)
#         self.cell(0, 10, 'Summary Report / सारांश रिपोर्ट', 0, 1, 'C')
#         self.ln(20)
#         if isinstance(self.summary, str):
#             self.multi_cell(0, 10, self.summary)
#         else:
#             self.set_font('HindiFont', '', 14) # increased font size for Hindi text
#             self.multi_cell(0, 10, self.summary) # removed 'decode' call



# def build_report(self):
#     self.add_page()
#     self.add_font('NotoSans', '', 'NotoSans-Regular.ttf', uni=True)
#     self.set_font('NotoSans', '', 12)
#     self.cell(0, 10, 'Summary Report / सारांश रिपोर्ट', 0, 1, 'C')
#     self.ln(20)
#     if isinstance(self.summary, str):
#         self.multi_cell(0, 10, self.summary)
#     else:
#         self.multi_cell(0, 10, self.summary.decode('utf-8'))