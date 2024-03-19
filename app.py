import grpc
from lnd_connection import connection_lnd,ln

def get_amount_sat():
    while True:
        try:
            amount_sat = int(input("Digita la cantidad en satoshis:"))
            if amount_sat > 0:
                return amount_sat
            else:
                print("El monto debe ser un entero mayor a cero. Por favor, inténtalo nuevamente!")
        except ValueError:
            print("Por favor, introduce un número entero válido!")

amount_sat = get_amount_sat()
comment = input("Escribe una descripción:(opcional)")

invoice_req = ln.Invoice(
    value=amount_sat,
    memo=comment
)

conn_lnd = connection_lnd("invoice")

try:
    rs = conn_lnd.AddInvoice(invoice_req)    
    print (rs.payment_request)
except grpc.RpcError as e:
    print(f"Error: e_status={e.code()} message={e.details()} debug={e.debug_error_string()}")
    