import bpy, os

def PAK_Update_EnableExport(self, context):
    """
    Updates the "Enable Export" property for all selected images
    """

    try:
        addon_prefs = context.preferences.addons[__package__].preferences
        file_data = bpy.data.objects[addon_prefs.default_datablock].PAK_FileData
    except KeyError:
        return
    
    if file_data.is_internal_update:
        return
    
    value = file_data.proxy_enable_export

    if file_data.enable_multiselect:
        for bundle in file_data.bundles:
            if bundle.is_selected:
                bundle.enable_export = value

    else:
        bundle = file_data.bundles[file_data.bundles_list_index].bundle_items
        for tex in bundle:
            tex.PAK_Img.enable_export = value

    return None

def PAK_Update_ExportLocation(self, context):
    """
    Updates the "Export Location" property for all selected images
    """

    try:
        addon_prefs = context.preferences.addons[__package__].preferences
        file_data = bpy.data.objects[addon_prefs.default_datablock].PAK_FileData
    except KeyError:
        return
    
    if file_data.is_internal_update:
        return
    
    value = file_data.proxy_export_location

    if file_data.enable_multiselect:
        for bundle in file_data.bundles:
            if bundle.is_selected:
                bundle.export_location = value

    else:
        bundle = file_data.bundles[file_data.bundles_list_index].bundle_items
        for tex in bundle:
            tex.PAK_Img.export_location = value

    return None

def PAK_Update_EnableBundles(self, context):
    """
    Automatically refreshes the list when the Enable Bundles is toggled 
    in order to provide the right data.
    """

    bpy.ops.pak.refresh_images()



def PAK_Update_TextureListItem_Name(self, context):
    """
    Updates the name of a texture bundle from the list UI.
    """

    # TODO: What is self in this context?

    try:
        addon_prefs = context.preferences.addons[__package__].preferences
        file_data = bpy.data.objects[addon_prefs.default_datablock].PAK_FileData
    except KeyError:
        return
    
    if file_data.is_internal_update:
        return
    
    value = self.name

    if file_data.enable_bundles is not True:
        for bundle_item in self.bundle_items:
            bundle_item.tex.name = value
    
    else:
        material_slot_names = [t.text for t in addon_prefs.material_slot_names]

        for bundle_item in self.bundle_items:
            tex = bundle_item.tex
            name = os.path.splitext(tex.name)
            filename = name[0]

            match = next(filter(filename.endswith, material_slot_names), None)
            new_name = value + match + name[1]
            tex.name = new_name



def PAK_Update_TextureListItem_EnableExport(self, context):
    """
    Updates the Enable Export property of a texture bundle from the list UI.
    """

    try:
        addon_prefs = context.preferences.addons[__package__].preferences
        file_data = bpy.data.objects[addon_prefs.default_datablock].PAK_FileData
    except KeyError:
        return

    if file_data.is_internal_update:
        return
    
    value = self.enable_export

    for bundle_item in self.bundle_items:
        bundle_item.tex.PAK_Img.enable_export = value
        

def PAK_Update_TextureListItem_ExportLocation(self, context):
    """
    Updates the Enable Export property of a texture bundle from the list UI.
    """

    try:
        addon_prefs = context.preferences.addons[__package__].preferences
        file_data = bpy.data.objects[addon_prefs.default_datablock].PAK_FileData
    except KeyError:
        return

    if file_data.is_internal_update:
        return
    
    
    value = self.export_location

    for bundle_item in self.bundle_items:
        bundle_item.tex.PAK_Img.export_location = value
