import sys
import os
import pathlib


sys.path.append(str(pathlib.Path(os.path.dirname(sys.path[0])).absolute()))
sys.path.append(str(pathlib.Path(os.path.dirname(sys.path[0]), 'test').absolute()))

import unittest
from .helpUnitTest import runGeneratorCommandHelp


class TestCLI(unittest.TestCase):
    
    def testGeneratorCommandHelp(self):
      return runGeneratorCommandHelp()
  
    def testDownloadCommandgdbcApiBySchemaFileRelPath(self):
      return runDownloadCommandgdbcApiBySchemaFileRelPath()
  
    def testGenerateCommandGeoDBCitiesBySchemaFileRelPath(self):
      return runGenerateCommandGeoDBCitiesBySchemaFileRelPath()
  
    def testGenerateCommandGeoDBCitiesByApiRelPath(self):
      return runGenerateCommandGeoDBCitiesByApiRelPath()
  
    # def testDownloadCommandGithubBySchemaFileRelPath(self):
    #   return runDownloadCommandGithubBySchemaFileRelPath()
  
    # def testGenerateCommandGithubByApiAbsPath(self):
    #   return runGenerateCommandGithubByApiAbsPath()
  
    def testGenerateCommandGithubBySchemaFile(self):
      return runGenerateCommandGithubBySchemaFile()
  
    def testDownloadCommandRapidApiBySchemaFileRelPath(self):
      return runDownloadCommandRapidApiBySchemaFileRelPath()
  
    def testGenerateCommandRapidApiByApiAbsPath(self):
      return runGenerateCommandRapidApiByApiAbsPath()



def runDownloadCommandgdbcApiBySchemaFileRelPath():
    print('\nRunning runDownloadCommandGithubBySchemaFileRelPath...')
    command = "pygqlcodegen download ./commandsOutput/Github/schema.json -apiArgs ./tests/cliInput/GdbcApi/downloaderArgs.json" #command to be executed
    print("Launching: " + command)
        
    res = os.system(command)
    print("End of runDownloadCommandGithubBySchemaFileRelPath")
    
def runGenerateCommandGeoDBCitiesBySchemaFileRelPath():
    print('\nRunning runGenerateCommandGeoDBCitiesBySchemaFileRelPath...')
    command = "pygqlcodegen generate ./commandsOutput/GeoDBCities -apiArgs tests/cliInput/GdbcApi/schema.json" #command to be executed
    print("Launching: " + command)
        
    res = os.system(command)
    print("End of runGenerateCommandGeoDBCitiesBySchemaFileRelPath")
    
def runGenerateCommandGeoDBCitiesByApiRelPath():
    print('\nRunning runGenerateCommandGeoDBCitiesByApiRelPath...')
    command = "pygqlcodegen generate C:/Users/compl/Desktop/Python/proj/py-graphql-mapper/tests/commandsOutput/GeoDBCities -apiArgs C:/Users/compl/Desktop/Python/proj/PyGraphQLHelper/test/GraphQLClients/gdbcApi/generatorArgs.json -v" #command to be executed
    print("Launching: " + command)
    
    res = os.system(command)
    print("End of runGenerateCommandGeoDBCitiesByApiRelPath")


def runDownloadCommandGithubBySchemaFileRelPath():
    print('\nRunning runDownloadCommandGithubBySchemaFileRelPath...')
    command = "pygqlcodegen download ./tests/commandsOutput/Github/schema.json -apiArgs C:/Users/compl/Desktop/Python/proj/PyGraphQLHelper/test/GraphQLClients/GithubApi/downloaderArgs.json" #command to be executed
    print("Launching: " + command)
        
    res = os.system(command)
    print("End of runDownloadCommandGithubBySchemaFileRelPath")
    
def runGenerateCommandGithubByApiAbsPath():
    print('\nRunning runGenerateCommandGithubByApiAbsPath...')
    command = "pygqlcodegen generate ./tests/commandsOutput/Github -v -apiArgs C:/Users/compl/Desktop/Python/proj/PyGraphQLHelper/test/GraphQLClients/GithubApi/generatorArgs.json" #command to be executed
    print("Launching: " + command)
    
    res = os.system(command)
    print("End of runGenerateCommandGithubByApiAbsPath")
    
def runGenerateCommandGithubBySchemaFile():
    print('\nRunning runGenerateCommandGithubByApiAbsPath...')
    command = "pygqlcodegen generate ./tests/commandsOutput/Github -v -apiArgs C:/Users/compl/Desktop/Python/proj/PyGraphQLHelper/test/GraphQLClients/GithubApi/generatorArgs.json" #command to be executed
    print("Launching: " + command)
    
    res = os.system(command)
    print("End of runGenerateCommandGithubByApiAbsPath")

def runDownloadCommandRapidApiBySchemaFileRelPath():
    print('\nRunning runDownloadCommandRapidApiBySchemaFileRelPath...')
    command = "pygqlcodegen download ./tests/commandsOutput/RapidApi/schema.json -apiArgs ./test/GraphQLClients/RapidApi/downloaderArgs.json" #command to be executed
    print("Launching: " + command)
        
    res = os.system(command)
    print("End of runDownloadCommandRapidApiBySchemaFileRelPath")
    
def runGenerateCommandRapidApiByApiAbsPath():
    print('\nRunning runGenerateCommandRapidApiByApiAbsPath...')
    command = "pygqlcodegen generate ./tests/commandsOutput/RapidApi -v -apiArgs C:/Users/compl/Desktop/Python/proj/PyGraphQLHelper/test/GraphQLClients/RapidApi/generatorArgs.json" #command to be executed
    print("Launching: " + command)
    
    res = os.system(command)
    print("End of runGenerateCommandRapidApiByApiAbsPath")
    