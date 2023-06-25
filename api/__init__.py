from fastapi import APIRouter

from api import customer,product,max_order,orders,total_sales,total_profit

api_router=APIRouter()

api_router.include_router(customer.router)
api_router.include_router(product.router)
api_router.include_router(max_order.router)
api_router.include_router(orders.router)
api_router.include_router(total_sales.router)
api_router.include_router(total_profit.router)
