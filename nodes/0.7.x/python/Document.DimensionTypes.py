import System
import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager

doc = DocumentManager.Instance.CurrentDBDocument

elementlist = list()
collector = FilteredElementCollector(doc)
collector.OfClass(DimensionType)
OUT = collector.ToElements()