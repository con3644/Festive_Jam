#This script was generated with the addons Blender for UnrealEngine : https://github.com/xavier150/Blender-For-UnrealEngine-Addons
#It will import into Unreal Engine all the assets of type StaticMesh, SkeletalMesh, Animation and Pose
#The script must be used in Unreal Engine Editor with UnrealEnginePython : https://github.com/20tab/UnrealEnginePython

import os.path
import unreal_engine as ue
from unreal_engine.classes import PyFbxFactory
from unreal_engine.enums import EFBXImportType, EMaterialSearchLocation

#Prepare var and process import
UnrealImportLocation = r'/Game/ImportedFbx'
ImportedAsset = []

print('========================= Import started ! =========================')



################[ Import Armature as SkeletalMesh type ]################
fbx_factory = PyFbxFactory()
fbx_factory.ImportUI.bImportMaterials = True
fbx_factory.ImportUI.bImportTextures = False
fbx_factory.ImportUI.TextureImportData.MaterialSearchLocation = EMaterialSearchLocation.Local
fbx_factory.ImportUI.bImportAnimations = False
fbx_factory.ImportUI.SkeletalMeshImportData.bImportMorphTargets = True
fbx_factory.ImportUI.bCreatePhysicsAsset = True
FbxLoc = os.path.join(r'H:\Pictures\3dAssets\Starting Pack\Prototypes\ExportedFbx\SkeletalMesh\Armature\SK_Armature.fbx')
AssetImportLocation = os.path.join(UnrealImportLocation, r'').replace('\\','/')
AssetImportLocation = AssetImportLocation.rstrip('/')
try:
	asset = fbx_factory.factory_import_object(FbxLoc, AssetImportLocation)
	ImportedAsset.append(asset)
except:
	ImportedAsset.append('Import error for asset named "Armature" ')



################[ Import Armature as Animation type ]################
SkeletonLocation = os.path.join(UnrealImportLocation, r'SK_Armature_Skeleton.SK_Armature_Skeleton').replace('\\','/')
OriginSkeleton = ue.find_asset(SkeletonLocation)
if OriginSkeleton:
	fbx_factory = PyFbxFactory()
	fbx_factory.ImportUI.bImportMesh = False
	fbx_factory.ImportUI.bCreatePhysicsAsset = False
	fbx_factory.ImportUI.Skeleton = OriginSkeleton
	fbx_factory.ImportUI.bImportAnimations = True
	fbx_factory.ImportUI.MeshTypeToImport = EFBXImportType.FBXIT_Animation
	fbx_factory.ImportUI.SkeletalMeshImportData.bImportMorphTargets = True
	FbxLoc = os.path.join(r'H:\Pictures\3dAssets\Starting Pack\Prototypes\ExportedFbx\SkeletalMesh\Armature\Anim\Anim_Armature_Fist.fbx')
	AssetImportLocation = os.path.join(UnrealImportLocation, r'Anim').replace('\\','/')
	AssetImportLocation = AssetImportLocation.rstrip('/')
	try:
		asset = fbx_factory.factory_import_object(FbxLoc, AssetImportLocation)
		ImportedAsset.append(asset)
	except:
		ImportedAsset.append('Import error for asset named "Armature" ')
else:
	ImportedAsset.append('Skeleton "'+SkeletonLocation+'" Not found for "Armature" asset ')



################[ Import Armature as Pose type ]################
SkeletonLocation = os.path.join(UnrealImportLocation, r'SK_Armature_Skeleton.SK_Armature_Skeleton').replace('\\','/')
OriginSkeleton = ue.find_asset(SkeletonLocation)
if OriginSkeleton:
	fbx_factory = PyFbxFactory()
	fbx_factory.ImportUI.bImportMesh = False
	fbx_factory.ImportUI.bCreatePhysicsAsset = False
	fbx_factory.ImportUI.Skeleton = OriginSkeleton
	fbx_factory.ImportUI.bImportAnimations = True
	fbx_factory.ImportUI.MeshTypeToImport = EFBXImportType.FBXIT_Animation
	fbx_factory.ImportUI.SkeletalMeshImportData.bImportMorphTargets = True
	FbxLoc = os.path.join(r'H:\Pictures\3dAssets\Starting Pack\Prototypes\ExportedFbx\SkeletalMesh\Armature\Anim\Pose_Armature_Grip.fbx')
	AssetImportLocation = os.path.join(UnrealImportLocation, r'Anim').replace('\\','/')
	AssetImportLocation = AssetImportLocation.rstrip('/')
	try:
		asset = fbx_factory.factory_import_object(FbxLoc, AssetImportLocation)
		ImportedAsset.append(asset)
	except:
		ImportedAsset.append('Import error for asset named "Armature" ')
else:
	ImportedAsset.append('Skeleton "'+SkeletonLocation+'" Not found for "Armature" asset ')



################[ Import Armature as Pose type ]################
SkeletonLocation = os.path.join(UnrealImportLocation, r'SK_Armature_Skeleton.SK_Armature_Skeleton').replace('\\','/')
OriginSkeleton = ue.find_asset(SkeletonLocation)
if OriginSkeleton:
	fbx_factory = PyFbxFactory()
	fbx_factory.ImportUI.bImportMesh = False
	fbx_factory.ImportUI.bCreatePhysicsAsset = False
	fbx_factory.ImportUI.Skeleton = OriginSkeleton
	fbx_factory.ImportUI.bImportAnimations = True
	fbx_factory.ImportUI.MeshTypeToImport = EFBXImportType.FBXIT_Animation
	fbx_factory.ImportUI.SkeletalMeshImportData.bImportMorphTargets = True
	FbxLoc = os.path.join(r'H:\Pictures\3dAssets\Starting Pack\Prototypes\ExportedFbx\SkeletalMesh\Armature\Anim\Pose_Armature_Grip hold.fbx')
	AssetImportLocation = os.path.join(UnrealImportLocation, r'Anim').replace('\\','/')
	AssetImportLocation = AssetImportLocation.rstrip('/')
	try:
		asset = fbx_factory.factory_import_object(FbxLoc, AssetImportLocation)
		ImportedAsset.append(asset)
	except:
		ImportedAsset.append('Import error for asset named "Armature" ')
else:
	ImportedAsset.append('Skeleton "'+SkeletonLocation+'" Not found for "Armature" asset ')



################[ Import Armature as Animation type ]################
SkeletonLocation = os.path.join(UnrealImportLocation, r'SK_Armature_Skeleton.SK_Armature_Skeleton').replace('\\','/')
OriginSkeleton = ue.find_asset(SkeletonLocation)
if OriginSkeleton:
	fbx_factory = PyFbxFactory()
	fbx_factory.ImportUI.bImportMesh = False
	fbx_factory.ImportUI.bCreatePhysicsAsset = False
	fbx_factory.ImportUI.Skeleton = OriginSkeleton
	fbx_factory.ImportUI.bImportAnimations = True
	fbx_factory.ImportUI.MeshTypeToImport = EFBXImportType.FBXIT_Animation
	fbx_factory.ImportUI.SkeletalMeshImportData.bImportMorphTargets = True
	FbxLoc = os.path.join(r'H:\Pictures\3dAssets\Starting Pack\Prototypes\ExportedFbx\SkeletalMesh\Armature\Anim\Anim_Armature_Grip Sword SwingHorizontal.fbx')
	AssetImportLocation = os.path.join(UnrealImportLocation, r'Anim').replace('\\','/')
	AssetImportLocation = AssetImportLocation.rstrip('/')
	try:
		asset = fbx_factory.factory_import_object(FbxLoc, AssetImportLocation)
		ImportedAsset.append(asset)
	except:
		ImportedAsset.append('Import error for asset named "Armature" ')
else:
	ImportedAsset.append('Skeleton "'+SkeletonLocation+'" Not found for "Armature" asset ')



################[ Import Armature as Animation type ]################
SkeletonLocation = os.path.join(UnrealImportLocation, r'SK_Armature_Skeleton.SK_Armature_Skeleton').replace('\\','/')
OriginSkeleton = ue.find_asset(SkeletonLocation)
if OriginSkeleton:
	fbx_factory = PyFbxFactory()
	fbx_factory.ImportUI.bImportMesh = False
	fbx_factory.ImportUI.bCreatePhysicsAsset = False
	fbx_factory.ImportUI.Skeleton = OriginSkeleton
	fbx_factory.ImportUI.bImportAnimations = True
	fbx_factory.ImportUI.MeshTypeToImport = EFBXImportType.FBXIT_Animation
	fbx_factory.ImportUI.SkeletalMeshImportData.bImportMorphTargets = True
	FbxLoc = os.path.join(r'H:\Pictures\3dAssets\Starting Pack\Prototypes\ExportedFbx\SkeletalMesh\Armature\Anim\Anim_Armature_Grip Sword SwingVerticle.fbx')
	AssetImportLocation = os.path.join(UnrealImportLocation, r'Anim').replace('\\','/')
	AssetImportLocation = AssetImportLocation.rstrip('/')
	try:
		asset = fbx_factory.factory_import_object(FbxLoc, AssetImportLocation)
		ImportedAsset.append(asset)
	except:
		ImportedAsset.append('Import error for asset named "Armature" ')
else:
	ImportedAsset.append('Skeleton "'+SkeletonLocation+'" Not found for "Armature" asset ')



################[ Import Armature as Pose type ]################
SkeletonLocation = os.path.join(UnrealImportLocation, r'SK_Armature_Skeleton.SK_Armature_Skeleton').replace('\\','/')
OriginSkeleton = ue.find_asset(SkeletonLocation)
if OriginSkeleton:
	fbx_factory = PyFbxFactory()
	fbx_factory.ImportUI.bImportMesh = False
	fbx_factory.ImportUI.bCreatePhysicsAsset = False
	fbx_factory.ImportUI.Skeleton = OriginSkeleton
	fbx_factory.ImportUI.bImportAnimations = True
	fbx_factory.ImportUI.MeshTypeToImport = EFBXImportType.FBXIT_Animation
	fbx_factory.ImportUI.SkeletalMeshImportData.bImportMorphTargets = True
	FbxLoc = os.path.join(r'H:\Pictures\3dAssets\Starting Pack\Prototypes\ExportedFbx\SkeletalMesh\Armature\Anim\Pose_Armature_Grip Wand.fbx')
	AssetImportLocation = os.path.join(UnrealImportLocation, r'Anim').replace('\\','/')
	AssetImportLocation = AssetImportLocation.rstrip('/')
	try:
		asset = fbx_factory.factory_import_object(FbxLoc, AssetImportLocation)
		ImportedAsset.append(asset)
	except:
		ImportedAsset.append('Import error for asset named "Armature" ')
else:
	ImportedAsset.append('Skeleton "'+SkeletonLocation+'" Not found for "Armature" asset ')



################[ Import Armature as Pose type ]################
SkeletonLocation = os.path.join(UnrealImportLocation, r'SK_Armature_Skeleton.SK_Armature_Skeleton').replace('\\','/')
OriginSkeleton = ue.find_asset(SkeletonLocation)
if OriginSkeleton:
	fbx_factory = PyFbxFactory()
	fbx_factory.ImportUI.bImportMesh = False
	fbx_factory.ImportUI.bCreatePhysicsAsset = False
	fbx_factory.ImportUI.Skeleton = OriginSkeleton
	fbx_factory.ImportUI.bImportAnimations = True
	fbx_factory.ImportUI.MeshTypeToImport = EFBXImportType.FBXIT_Animation
	fbx_factory.ImportUI.SkeletalMeshImportData.bImportMorphTargets = True
	FbxLoc = os.path.join(r'H:\Pictures\3dAssets\Starting Pack\Prototypes\ExportedFbx\SkeletalMesh\Armature\Anim\Pose_Armature_Grip Wandv2.fbx')
	AssetImportLocation = os.path.join(UnrealImportLocation, r'Anim').replace('\\','/')
	AssetImportLocation = AssetImportLocation.rstrip('/')
	try:
		asset = fbx_factory.factory_import_object(FbxLoc, AssetImportLocation)
		ImportedAsset.append(asset)
	except:
		ImportedAsset.append('Import error for asset named "Armature" ')
else:
	ImportedAsset.append('Skeleton "'+SkeletonLocation+'" Not found for "Armature" asset ')



################[ Import Armature as Animation type ]################
SkeletonLocation = os.path.join(UnrealImportLocation, r'SK_Armature_Skeleton.SK_Armature_Skeleton').replace('\\','/')
OriginSkeleton = ue.find_asset(SkeletonLocation)
if OriginSkeleton:
	fbx_factory = PyFbxFactory()
	fbx_factory.ImportUI.bImportMesh = False
	fbx_factory.ImportUI.bCreatePhysicsAsset = False
	fbx_factory.ImportUI.Skeleton = OriginSkeleton
	fbx_factory.ImportUI.bImportAnimations = True
	fbx_factory.ImportUI.MeshTypeToImport = EFBXImportType.FBXIT_Animation
	fbx_factory.ImportUI.SkeletalMeshImportData.bImportMorphTargets = True
	FbxLoc = os.path.join(r'H:\Pictures\3dAssets\Starting Pack\Prototypes\ExportedFbx\SkeletalMesh\Armature\Anim\Anim_Armature_Horizontal swing.fbx')
	AssetImportLocation = os.path.join(UnrealImportLocation, r'Anim').replace('\\','/')
	AssetImportLocation = AssetImportLocation.rstrip('/')
	try:
		asset = fbx_factory.factory_import_object(FbxLoc, AssetImportLocation)
		ImportedAsset.append(asset)
	except:
		ImportedAsset.append('Import error for asset named "Armature" ')
else:
	ImportedAsset.append('Skeleton "'+SkeletonLocation+'" Not found for "Armature" asset ')



################[ Import Armature as Pose type ]################
SkeletonLocation = os.path.join(UnrealImportLocation, r'SK_Armature_Skeleton.SK_Armature_Skeleton').replace('\\','/')
OriginSkeleton = ue.find_asset(SkeletonLocation)
if OriginSkeleton:
	fbx_factory = PyFbxFactory()
	fbx_factory.ImportUI.bImportMesh = False
	fbx_factory.ImportUI.bCreatePhysicsAsset = False
	fbx_factory.ImportUI.Skeleton = OriginSkeleton
	fbx_factory.ImportUI.bImportAnimations = True
	fbx_factory.ImportUI.MeshTypeToImport = EFBXImportType.FBXIT_Animation
	fbx_factory.ImportUI.SkeletalMeshImportData.bImportMorphTargets = True
	FbxLoc = os.path.join(r'H:\Pictures\3dAssets\Starting Pack\Prototypes\ExportedFbx\SkeletalMesh\Armature\Anim\Pose_Armature_Idle1.fbx')
	AssetImportLocation = os.path.join(UnrealImportLocation, r'Anim').replace('\\','/')
	AssetImportLocation = AssetImportLocation.rstrip('/')
	try:
		asset = fbx_factory.factory_import_object(FbxLoc, AssetImportLocation)
		ImportedAsset.append(asset)
	except:
		ImportedAsset.append('Import error for asset named "Armature" ')
else:
	ImportedAsset.append('Skeleton "'+SkeletonLocation+'" Not found for "Armature" asset ')



################[ Import Armature as Pose type ]################
SkeletonLocation = os.path.join(UnrealImportLocation, r'SK_Armature_Skeleton.SK_Armature_Skeleton').replace('\\','/')
OriginSkeleton = ue.find_asset(SkeletonLocation)
if OriginSkeleton:
	fbx_factory = PyFbxFactory()
	fbx_factory.ImportUI.bImportMesh = False
	fbx_factory.ImportUI.bCreatePhysicsAsset = False
	fbx_factory.ImportUI.Skeleton = OriginSkeleton
	fbx_factory.ImportUI.bImportAnimations = True
	fbx_factory.ImportUI.MeshTypeToImport = EFBXImportType.FBXIT_Animation
	fbx_factory.ImportUI.SkeletalMeshImportData.bImportMorphTargets = True
	FbxLoc = os.path.join(r'H:\Pictures\3dAssets\Starting Pack\Prototypes\ExportedFbx\SkeletalMesh\Armature\Anim\Pose_Armature_Idlev2.fbx')
	AssetImportLocation = os.path.join(UnrealImportLocation, r'Anim').replace('\\','/')
	AssetImportLocation = AssetImportLocation.rstrip('/')
	try:
		asset = fbx_factory.factory_import_object(FbxLoc, AssetImportLocation)
		ImportedAsset.append(asset)
	except:
		ImportedAsset.append('Import error for asset named "Armature" ')
else:
	ImportedAsset.append('Skeleton "'+SkeletonLocation+'" Not found for "Armature" asset ')



################[ Import Armature as Animation type ]################
SkeletonLocation = os.path.join(UnrealImportLocation, r'SK_Armature_Skeleton.SK_Armature_Skeleton').replace('\\','/')
OriginSkeleton = ue.find_asset(SkeletonLocation)
if OriginSkeleton:
	fbx_factory = PyFbxFactory()
	fbx_factory.ImportUI.bImportMesh = False
	fbx_factory.ImportUI.bCreatePhysicsAsset = False
	fbx_factory.ImportUI.Skeleton = OriginSkeleton
	fbx_factory.ImportUI.bImportAnimations = True
	fbx_factory.ImportUI.MeshTypeToImport = EFBXImportType.FBXIT_Animation
	fbx_factory.ImportUI.SkeletalMeshImportData.bImportMorphTargets = True
	FbxLoc = os.path.join(r'H:\Pictures\3dAssets\Starting Pack\Prototypes\ExportedFbx\SkeletalMesh\Armature\Anim\Anim_Armature_Point.fbx')
	AssetImportLocation = os.path.join(UnrealImportLocation, r'Anim').replace('\\','/')
	AssetImportLocation = AssetImportLocation.rstrip('/')
	try:
		asset = fbx_factory.factory_import_object(FbxLoc, AssetImportLocation)
		ImportedAsset.append(asset)
	except:
		ImportedAsset.append('Import error for asset named "Armature" ')
else:
	ImportedAsset.append('Skeleton "'+SkeletonLocation+'" Not found for "Armature" asset ')



################[ Import Armature as Animation type ]################
SkeletonLocation = os.path.join(UnrealImportLocation, r'SK_Armature_Skeleton.SK_Armature_Skeleton').replace('\\','/')
OriginSkeleton = ue.find_asset(SkeletonLocation)
if OriginSkeleton:
	fbx_factory = PyFbxFactory()
	fbx_factory.ImportUI.bImportMesh = False
	fbx_factory.ImportUI.bCreatePhysicsAsset = False
	fbx_factory.ImportUI.Skeleton = OriginSkeleton
	fbx_factory.ImportUI.bImportAnimations = True
	fbx_factory.ImportUI.MeshTypeToImport = EFBXImportType.FBXIT_Animation
	fbx_factory.ImportUI.SkeletalMeshImportData.bImportMorphTargets = True
	FbxLoc = os.path.join(r'H:\Pictures\3dAssets\Starting Pack\Prototypes\ExportedFbx\SkeletalMesh\Armature\Anim\Anim_Armature_ThumbUp.fbx')
	AssetImportLocation = os.path.join(UnrealImportLocation, r'Anim').replace('\\','/')
	AssetImportLocation = AssetImportLocation.rstrip('/')
	try:
		asset = fbx_factory.factory_import_object(FbxLoc, AssetImportLocation)
		ImportedAsset.append(asset)
	except:
		ImportedAsset.append('Import error for asset named "Armature" ')
else:
	ImportedAsset.append('Skeleton "'+SkeletonLocation+'" Not found for "Armature" asset ')



################[ Import Armature as Animation type ]################
SkeletonLocation = os.path.join(UnrealImportLocation, r'SK_Armature_Skeleton.SK_Armature_Skeleton').replace('\\','/')
OriginSkeleton = ue.find_asset(SkeletonLocation)
if OriginSkeleton:
	fbx_factory = PyFbxFactory()
	fbx_factory.ImportUI.bImportMesh = False
	fbx_factory.ImportUI.bCreatePhysicsAsset = False
	fbx_factory.ImportUI.Skeleton = OriginSkeleton
	fbx_factory.ImportUI.bImportAnimations = True
	fbx_factory.ImportUI.MeshTypeToImport = EFBXImportType.FBXIT_Animation
	fbx_factory.ImportUI.SkeletalMeshImportData.bImportMorphTargets = True
	FbxLoc = os.path.join(r'H:\Pictures\3dAssets\Starting Pack\Prototypes\ExportedFbx\SkeletalMesh\Armature\Anim\Anim_Armature_Verticle swing.fbx')
	AssetImportLocation = os.path.join(UnrealImportLocation, r'Anim').replace('\\','/')
	AssetImportLocation = AssetImportLocation.rstrip('/')
	try:
		asset = fbx_factory.factory_import_object(FbxLoc, AssetImportLocation)
		ImportedAsset.append(asset)
	except:
		ImportedAsset.append('Import error for asset named "Armature" ')
else:
	ImportedAsset.append('Skeleton "'+SkeletonLocation+'" Not found for "Armature" asset ')



################[ Import Cube as StaticMesh type ]################
fbx_factory = PyFbxFactory()
fbx_factory.ImportUI.bImportMaterials = True
fbx_factory.ImportUI.bImportTextures = False
fbx_factory.ImportUI.TextureImportData.MaterialSearchLocation = EMaterialSearchLocation.Local
fbx_factory.ImportUI.StaticMeshImportData.bCombineMeshes = True
fbx_factory.ImportUI.StaticMeshImportData.bAutoGenerateCollision = False
fbx_factory.ImportUI.StaticMeshImportData.bGenerateLightmapUVs = True
FbxLoc = os.path.join(r'H:\Pictures\3dAssets\Starting Pack\Prototypes\ExportedFbx\StaticMesh\SM_Cube.fbx')
AssetImportLocation = os.path.join(UnrealImportLocation, r'').replace('\\','/')
AssetImportLocation = AssetImportLocation.rstrip('/')
try:
	asset = fbx_factory.factory_import_object(FbxLoc, AssetImportLocation)
	ImportedAsset.append(asset)
except:
	ImportedAsset.append('Import error for asset named "Cube" ')



print('========================= Imports completed ! =========================')

for asset in ImportedAsset:
	print(asset)

print('=========================')
