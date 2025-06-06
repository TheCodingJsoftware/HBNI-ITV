from app.handlers.api.assignment import AssignmentAPIHandler
from app.handlers.api.google_share_folder_ids import SharedGoogleFolderIDsAPIHandler
from app.handlers.api.login import LoginAPIHandler
from app.handlers.api.logout import LogoutAPIHandler
from app.handlers.api.news import NewsAPIHandler
from app.handlers.api.recordings import RecordingsAPIHandler
from app.handlers.api.register import RegisterAPIHandler
from app.handlers.api.thumbnail import ThumbnailProxyHandler
from app.routes.helpers import route

api_routes = [
    route(r"/api/news", NewsAPIHandler, name="api_news"),
    route(r"/api/login", LoginAPIHandler, name="api_login"),
    route(r"/api/logout", LogoutAPIHandler, name="api_logout"),
    route(r"/api/register", RegisterAPIHandler, name="api_register"),
    route(r"/api/assignment", AssignmentAPIHandler, name="api_assignment"),
    route(r"/api/recordings", RecordingsAPIHandler, name="api_recordings"),
    route(r"/api/thumbnail", ThumbnailProxyHandler, name="api_thumbnail"),
    route(
        r"/api/shared_google_folder_ids",
        SharedGoogleFolderIDsAPIHandler,
        name="api_shared_google_folder_ids",
    ),
]
