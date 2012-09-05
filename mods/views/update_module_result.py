<<<<<<< HEAD
#coding: utf-8
from django.shortcuts import HttpResponse, render_to_response
from django.http import HttpResponseRedirect
from django import template
import time
from mods.models import Mod, ModJSRequire, ModCSSRequire, ModLayoutSupport, attach
from util.upload import Upload
from settings import FILE_UPLOAD_PATH
def updateModuleResult(request):
    if request.method == "POST" :
        form =  request.POST
        modId  = form.get("form_id")
        #保存上传的附件
        if request.FILES.getlist('img_thumb'):
                uploadAttach = request.FILES.getlist('img_thumb')
                dbAttach = Upload().saveAttach(uploadAttach)
                attachId = dbAttach['attachId']
                imgThumb = FILE_UPLOAD_PATH + dbAttach['file_path']
                
        #更新mod表记录
        mod = Mod.objects.filter(id = modId)[0]
        mod.img_thumb =  imgThumb
        mod.type_id =  form.get("type")
        mod.html_tpl_str =  form.get("html_tpl_str")
        mod.demo_json_str =  form.get("demo_json_str")
        mod.last_modified_time =  time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        mod.isOnline = False
        mod.save()
        
        #更新mod_js_require表记录
        ModJSRequire.objects.filter(id = modId).delete()
        jsRequire = form.get("mod_js_require")
        jsUrlList = jsRequire.split('\r\n')
        for jsUrl in jsUrlList :
            
            ModJSRequireTable = ModJSRequire(
                                        mod_id =  int(modId),
                                        url = jsUrl,
                                        index = jsUrlList.index(jsUrl)
                                        )
            ModJSRequireTable.save()
        
        #更新mod_css_require表记录 
        cssRequire = form.get("mod_css_require")
        cssUrlList = cssRequire.split('\r\n')
        for cssUrl in cssUrlList :
            ModCSSRequireTable = ModCSSRequire(
                                       mod_id = int(modId),
                                        url = cssUrl,
                                        index = cssUrlList.index(cssUrl)
                                        )
            ModCSSRequireTable.save()
        
        #更新mod_layout_support表记录
        ModLayoutSupport.objects.filter(mod = modId).delete()
        checkbox_list = request.REQUEST.getlist('check_box_list')
        for checkedField in checkbox_list :
            print checkedField
        for checkedField in checkbox_list :
            ModLayoutSupportTable = ModLayoutSupport(
                                        mod_id =  int(modId),
                                        layout_type = checkedField
                                        )
            ModLayoutSupportTable.save()
            
        return HttpResponse('OK')
=======
#coding: utf-8
from django.shortcuts import HttpResponse, render_to_response
from django.http import HttpResponseRedirect
from django import template
import time
from mods.models import Mod, ModJSRequire, ModCSSRequire, ModLayoutSupport, attach
from util.upload import Upload
from settings import FILE_UPLOAD_PATH
def updateModuleResult(request):
    if request.method == "POST" :
        form =  request.POST
        modId  = form.get("form_id")
        #保存上传的附件
        if request.FILES.getlist('img_thumb'):
                uploadAttach = request.FILES.getlist('img_thumb')
                dbAttach = Upload().saveAttach(uploadAttach)
                attachId = dbAttach['attachId']
                imgThumb = FILE_UPLOAD_PATH + dbAttach['file_path']
                
        #更新mod表记录
        mod = Mod.objects.filter(id = modId)[0]
        mod.img_thumb =  imgThumb
        mod.type_id =  form.get("type")
        mod.html_tpl_str =  form.get("html_tpl_str")
        mod.demo_json_str =  form.get("demo_json_str")
        mod.last_modified_time =  time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        mod.isOnline = False
        mod.save()
        
        #更新mod_js_require表记录
        ModJSRequire.objects.filter(id = modId).delete()
        jsRequire = form.get("mod_js_require")
        jsUrlList = jsRequire.split('\r\n')
        for jsUrl in jsUrlList :
            
            ModJSRequireTable = ModJSRequire(
                                        mod_id =  int(modId),
                                        url = jsUrl,
                                        index = jsUrlList.index(jsUrl)
                                        )
            ModJSRequireTable.save()
        
        #更新mod_css_require表记录 
        cssRequire = form.get("mod_css_require")
        cssUrlList = cssRequire.split('\r\n')
        for cssUrl in cssUrlList :
            ModCSSRequireTable = ModCSSRequire(
                                       mod_id = int(modId),
                                        url = cssUrl,
                                        index = cssUrlList.index(cssUrl)
                                        )
            ModCSSRequireTable.save()
        
        #更新mod_layout_support表记录
        ModLayoutSupport.objects.filter(mod = modId).delete()
        checkbox_list = request.REQUEST.getlist('check_box_list')
        for checkedField in checkbox_list :
            print checkedField
        for checkedField in checkbox_list :
            ModLayoutSupportTable = ModLayoutSupport(
                                        mod_id =  int(modId),
                                        layout_type = checkedField
                                        )
            ModLayoutSupportTable.save()
            
        return HttpResponse('OK')
>>>>>>> 9cec4fa0859be2f9fe446359168e8d6b99f95dee
                