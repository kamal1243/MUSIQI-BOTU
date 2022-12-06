import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "18677149"))
    API_HASH = os.environ.get("API_HASH", "4fb2463e7bec8bb620830e8e938d06fb")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5844265319:AAE5I7HH9TFoileiDrpkD2sDna_QVmz-qTs")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1ApWapzMBu1CRMSAoLgsmrc5qbBs5r_qHsZtRhSBi2XWfvZ1tQOXtnKVt1ybX9b3JEUNTX0NCSFazdAuWXA8_mZ-3G1Bhp2yXjXaOYG-SlqAz-I4FRQsl0dOjjp-vLtoolt30G-3ziviDhO-6YWENarBTqcatpkBFYpCT2XyojZetWKd2FgyMkGv32JwqayrEPYH3B1ZA5pMdyk9RNoRhWiCY31Q6_oRE_RZMyfOXyyyZq49GnosxR_iIDJKVgBvmQywlvZh__LZ0BopefV8YY3qpNfYOCWuoKjdLCGyvvrVMpkThNidif6hZd2xwsGep_LmKQMgw2D9OI4vmunapzsQLgO8T_0c=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "GROOTMUSIC_robot")
    SUPPORT = os.environ.get("SUPPORT", "GROOTSERVICEMUSIC") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "GROOTSERVICEMUSIC") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/7af0ede8d54ad0b4610fd.jpg")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/e15386aa5dd916356c806.jpg")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "5532563304")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
