from flask_restful import Api
from resources.print import PrintCommandResource

PRINTER_API = Api(prefix='print')

# Print command
PRINTER_API.add_resource(PrintCommandResource, '/command/<int:id>')
