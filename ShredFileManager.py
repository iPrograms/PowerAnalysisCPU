
"""
ShredFileManager: shreds any single file into blocks,
depending on available remote servers
@Author MAnzoor Ahmed
@Date 10/04/2017
"""
import os

class ShredFileManager():
    
    def __init__(self,servers):
        
        self.servers = servers
        self.blocks = []
        self.block_number = -1
        self.start = 0
        self.end = 0

    # Show file size in bits        
    def fileInfoState(self, file):
        return os.stat(file).st_size

    # Generage meta data for each block
    def genBlockInfo(self, outterindex, index, starts, ends, data, path):
        return {"outterindex":outterindex2, index":index,"starts":starts, "ends":ends, "data":data,"path":path}
    
    # Show all blocks with meta tag
    def showPreparedBlocks(self):
        print(self.blocks)

    # Start shredding file
    def shred(self, file):
        size = self.fileInfoState(file)
        try:
            with open(file,"rb") as file:
                # Determine block size
                block_to_read = int(size / self.servers)            
                while True:
                    # Need to kow start and end of each block, for putting back together
                    self.end = int(block_to_read + self.start) 
                    byte = file.read(int(block_to_read))
                    if not byte:
                        break
                    print('%s',byte)
                    self.start = self.end
    
                    # Add store block meta data
                    self.blocks.append(self.genBlockInfo(self.start,self.end,byte,file.name))
        except FileNotFoundError as e:
            print('File Not Found!')
            pass
        except OSError as ose:
            print('OS Error!')
            pass
        
            #TODO before closing file, delete all content
            # No longer needed data
            file.close()
            print ('Done')
    def shuffleFile():
        
    
    
        
    
