import os
import sys
import clr

# Add a reference to the NMotive assembly
n_motive_dll_path = os.path.join(os.getcwd(), 'NMotive_API/NMotive.dll')
clr.AddReference(n_motive_dll_path)

# from NMotive import *
from NMotive import Take, CSVExporter, TRCExporter, LengthUnits, Rotation

def process_take(take, exporter_cls, file_extension, **exporter_params):
    exporter = exporter_cls()
    for param, value in exporter_params.items():
        setattr(exporter, param, value)
    
    path, full_filename = os.path.split(take.FileName)
    filename_no_extension, _ = os.path.splitext(full_filename)
    new_filename = os.path.join(path, filename_no_extension + file_extension)
    
    return exporter.Export(take, new_filename, True)

def process_folder(folder_path):
    for file in os.listdir(folder_path):
        if file.endswith('.tak'):
            file_path = os.path.join(folder_path, file)
            take = Take(file_path)
            
            # CSV 파일 내보내기
            process_take(take, CSVExporter, ".csv",
                         RotationType=Rotation.XYZ,
                         Units=LengthUnits.Units_Meters,
                         UseWorldSpaceCoordinates=True,
                         WriteBoneMarkers=False,
                         WriteBones=False,
                         WriteHeader=True,
                         WriteMarkers=False,
                         WriteQualityStats=True,
                         WriteRigidBodies=False,
                         WriteRigidBodyMarkers=False,
                         FrameRate=take.FrameRate,
                         StartFrame=take.FullFrameRange.get_Start(),
                         EndFrame=take.FullFrameRange.get_End())

            process_take(take, TRCExporter, ".trc", 
                         Units=LengthUnits.Units_Meters, 
                         FrameRate=take.FrameRate, 
                         StartFrame=take.FullFrameRange.get_Start(), 
                         EndFrame=take.FullFrameRange.get_End(), 
                         Scale=1)
            
            print(f"Processed {file} to CSV")

if __name__ == "__main__":
    folder_path = sys.argv[1]
    process_folder(folder_path)
