# encoding:utf-8

import plugins
from bridge.context import ContextType
from channel.chat_message import ChatMessage
from plugins import *

@plugins.register(
    name="mm",
    desire_priority=-1,
    hidden=True,
    desc="A simple plugin that member managerment system",
    version="0.1",
    author="wayne",
)
class mm(Plugin):
    def __init__(self):
        super().__init__()
        self.handlers[Event.ON_HANDLE_CONTEXT] = self.on_handle_context
        logger.info("[mm] inited")
        self.config = super().load_config()

    def on_handle_context(self, e_context: EventContext):
        if e_context["context"].type not in [
            ContextType.TEXT,
            ContextType.JOIN_GROUP,
            ContextType.PATPAT,
            ContextType.EXIT_GROUP
        ]:
            return

        # 使用 logger.info() 打印字典中的每个键值对，并使用 try/catch 逻辑处理非字符串值
        for key, value in e_context.econtext.items():
            try:
                logger.info(f"[econtext]{key}: {str(value)}\n")

                if key == "context":
                    logger.info(f"[econtext]{key}: {str(value['msg'])}\n")
            except Exception as e:
                logger.error(f"Error converting value for key '{key}': {e}")

        logger.info(
            "UserInfo: [" + str(e_context["context"]["msg"].actual_user_nickname) + " ] [ " + e_context["context"][
                "receiver"] + " ]")

    def get_help_text(self, **kwargs):
        help_text = "输入Hello，我会回复你的名字\n输入End，我会回复你世界的图片\n"
        return help_text
