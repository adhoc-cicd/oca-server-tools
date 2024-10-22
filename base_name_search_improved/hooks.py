import logging

_logger = logging.getLogger(__name__)


def post_init_hook(cr):
    cr["ir.model"].add_smart_search_to_models()
