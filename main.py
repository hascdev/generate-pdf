import jinja2
from xhtml2pdf import pisa

TEMPLATE_FILE = "template/template.html"

templateLoader = jinja2.FileSystemLoader(searchpath="./")
templateEnv = jinja2.Environment(loader=templateLoader)
template = templateEnv.get_template(TEMPLATE_FILE)

# This data can come from json file or database query
json_data = {
    "encabezado": {
        "nro_orden": "123ABCDFG",
        "cliente": "Alevergara78 alevergara78@gmail.com",
        "medio_pago": "Redcompra Webpay",
        "fecha_pago": "02 de Agosto de 2022 22:39",
        "total": "$ 64.000"
    },
    "pagos": [
        {
            "logo": "images/cge.png",
            "empresa": "CGE",
            "convenio": "CGE",
            "nro_cliente": "9533392",
            "nro_serie": "7D2F074A5",
            "monto": "$ 10.000"
        },
        {
            "logo": "images/cge.png",
            "empresa": "CGE",
            "convenio": "CGE",
            "nro_cliente": "9533392",
            "nro_serie": "7D2F074A5",
            "monto": "$ 20.000"
        },
        {
            "logo": "images/cge.png",
            "empresa": "CGE",
            "convenio": "CGE",
            "nro_cliente": "9533392",
            "nro_serie": "7D2F074A5",
            "monto": "$ 30.000"
        },
        {
            "logo": "images/cge.png",
            "empresa": "CGE",
            "convenio": "CGE",
            "nro_cliente": "9533392",
            "nro_serie": "7D2F074A5",
            "monto": "$ 40.000"
        },
        {
            "logo": "images/cge.png",
            "empresa": "CGE",
            "convenio": "CGE",
            "nro_cliente": "9533392",
            "nro_serie": "7D2F074A5",
            "monto": "$ 24.000"
        }
    ]
}

# This renders template with dynamic data 
source_html = template.render(encabezado=json_data["encabezado"], pagos=json_data["pagos"])

# print(source_html)

output_filename = "out/result.pdf"

# Utility function
def convert_html_to_pdf(source_html, output_filename):
    # open output file for writing (truncated binary)
    result_file = open(output_filename, "w+b")

    # convert HTML to PDF (https://xhtml2pdf.readthedocs.io/en/latest/usage.html)
    pisa_status = pisa.CreatePDF(
            source_html,                # the HTML to convert
            dest=result_file,
            encoding='UTF-8')           # file handle to recieve result

    # close output file
    result_file.close()                 # close output file

    # return False on success and True on errors
    return pisa_status.err

# Main program
if __name__ == "__main__":
    pisa.showLogging()
    convert_html_to_pdf(source_html.encode('UTF-8'), output_filename)