from pyramid.request import Request
from pyramid.response import Response
from pyramid.view import view_config

from svc1_first_auto_service.data.repository import Repository


@view_config(route_name='autos_api',
             request_method='GET',
             renderer='json')
def all_autos(_):
    cars = Repository.all_cars(limit=25)
    return cars


@view_config(route_name='auto_api',
             request_method='GET',
             renderer='json')
def single_auto(request: Request):
    car_id = request.matchdict.get('car_id')

    car = Repository.car_by_id(car_id)
    if not car:
        msg = "The car with id '{}' was not found.".format(car_id)
        return Response(status=404, json_body={'error': msg})

    return car


@view_config(route_name='auto',
             request_method='GET',
             renderer='json')
def auto_by_id(request: Request):
    cid = request.matchdict.get('cid')
    cid = int(cid)

    if cid is not None:
        car = Repository.car_by_cid(cid)
        if not car:
            msg = f"The car with id '{cid}' was not found."
            return Response(status=404, json_body={'error': msg})

        return car
    else:
        msg = f"The cid is None"
        return Response(status=404, json_body={'error': msg})
