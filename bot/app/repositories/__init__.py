from app.repositories.faq import Faq, FaqTypes, FaqAttachmentTypes
from app.repositories.text import Text
from app.repositories.ticket import Ticket
from app.repositories.user import User
from app.repositories.oauth import Oauth

repostitories = (
    Text,
    User,
    Faq,
    FaqTypes,
    FaqAttachmentTypes,
    Ticket,
    Oauth,

)
