from frostlight_engine import *

class SaveManager:

    def __init__(self,engine,path="data/saves/save.json"):
        self.engine = engine
        self.path = path
        
    def set_save_path(self,path:str) -> None:
        self.path = path

    def read_file(self) -> bool|dict:
        try:
            if not os.path.exists(self.path):
                self.write_file({})

            with open(self.path, 'rb') as file:
                data = file.read()
            if data:
                return json.loads(data)
            
        except Exception as e:
            self.engine.logger.error(e)
        
        return False
    
    def write_file(self,data:dict) -> bool:

        try:
            with open(self.path, "w+") as file:
                print(f"data: {data}, file: {file}")
                json.dump(data,file,ensure_ascii=True,indent=4,sort_keys=True)
                return True

        except Exception as e:
            self.engine.logger.error(e)
        return False


    def save(self,key,value)-> bool|dict:
        try:
            data = self.read_file()

            if data != False:
                data[key] = value
            else:
                data = {}

            self.write_file(data)
            return True
        except Exception as e:
            self.engine.logger.error(e)

        return False


    def load(self,key,default=None) -> any:
        if os.path.exists(self.path):
            try:
                data = self.read_file()
                if data != False :
                    if key in data:
                        return data[key]
                    else:
                        return default
                    
            except Exception as e:
                self.engine.logger.error(e)
        else:
            return default