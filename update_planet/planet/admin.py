# -*- coding: utf-8 -*-

from django.contrib import admin

from planet.models import (Blog, Generator, Feed, FeedLink, Post, PostLink,
    Author, PostAuthorData, Enclosure, Category, TagInfo)

from django.contrib.contenttypes.admin import GenericTabularInline
from tagging.models import TaggedItem, Tag
from tagging.forms import TagAdminForm


class PostLinkAdmin(admin.ModelAdmin):
    list_display = ("title", "rel", "mime_type", "post", "link")
    list_filter = ("rel", "mime_type")

admin.site.register(PostLink, PostLinkAdmin)


class PostAuthorDataAdmin(admin.ModelAdmin):
    list_display = ("author", "is_contributor", "post")
    list_filter = ("is_contributor", "author")

admin.site.register(PostAuthorData, PostAuthorDataAdmin)

class EnclosureAdmin(admin.ModelAdmin):
    list_display = ("post", "mime_type", "length", "link")
    list_filter = ("mime_type", )

admin.site.register(Enclosure, EnclosureAdmin)

class FeedAdmin(admin.ModelAdmin):
    list_display = ("title", "url", "blog", "language",
        "category", "etag", "last_modified", "last_checked", "is_active")
    list_filter = ("language", "generator", "category")
    search_fields = ["title", "url", "blog__title"]

admin.site.register(Feed, FeedAdmin)

class AuthorAdmin(admin.ModelAdmin):
    list_display = ("name", "email")
    search_fields = ["name"]

admin.site.register(Author, AuthorAdmin)

class EnclosureInline(admin.StackedInline):
    model = Enclosure
    extra = 0

class TaggedItemInline(GenericTabularInline):
    model = TaggedItem
    extra = 0

class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "feed", "guid", "date_created", "date_modified", "primary_tag")
    list_filter = ("feed", )
    #  list_filter = ("primary_tag",admin.RelatedOnlyFieldListFilter)
    search_fields = ["title", "feed__blog__title"]
    readonly_fields=('age', 'display_order')

    class Media:
        js = ( '/static/admin/js/dynamic_inlines_with_sort.js',)
        css = { 'all' : ['/static/admin/css/dynamic_inlines_with_sort.css'], }

    def get_form(self, request, obj=None, **kwargs):
        form = super(PostAdmin,self).get_form(request, obj, **kwargs)

        # form class is created per request by modelform_factory function
        # so it's safe to modify
        #we modify the the queryset
        form.base_fields['primary_tag'].queryset = obj.tags
        return form

admin.site.register(Post, PostAdmin, inlines=[TaggedItemInline,EnclosureInline])

class BlogAdmin(admin.ModelAdmin):
    list_display = ("title", "url", "date_created")
    search_fields = ["title", "url"]

admin.site.register(Blog, BlogAdmin)


class GeneratorAdmin(admin.ModelAdmin):
    list_display = ("name", "version", "link")

admin.site.register(Generator, GeneratorAdmin)

class FeedLinkAdmin(admin.ModelAdmin):
    list_display = ("feed", "mime_type", "rel", "link")
    list_filter = ("mime_type", "rel")

admin.site.register(FeedLink, FeedLinkAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ("title", )
    search_fields = ["title"]

admin.site.register(Category, CategoryAdmin)

class TagInfoAdmin(admin.ModelAdmin):
    list_display = ("tag","selector","ignore")
    readonly_fields = ["tag"]
    list_filter = ["selector","ignore"]
    search_fields = ["tag","date_modified"]
    list_editable = ["selector","ignore"]

    '''
    def get_readonly_fields(self, request, obj=None):
        if obj: # obj is not None, so this is an edit
            return ['third_party_id',] # Return a list or tuple of readonly fields' names
        else: # This is an addition
            return []
    '''

admin.site.register(TagInfo, TagInfoAdmin)

class TagInfoInline(admin.TabularInline):
    model = TagInfo
    extra = 0

class NewTagAdmin(admin.ModelAdmin):
    form = TagAdminForm

    '''
    list_display = ("title", "feed", "guid", "date_created", "date_modified", "primary_tag")
    list_filter = ("feed", )
    #  list_filter = ("primary_tag",admin.RelatedOnlyFieldListFilter)
    search_fields = ["title", "feed__blog__title"]
    readonly_fields=('age', 'display_order')

    class Media:
        js = ( '/static/admin/js/dynamic_inlines_with_sort.js',)
        css = { 'all' : ['/static/admin/css/dynamic_inlines_with_sort.css'], }

    def get_form(self, request, obj=None, **kwargs):
        form = super(PostAdmin,self).get_form(request, obj, **kwargs)

        # form class is created per request by modelform_factory function
        # so it's safe to modify
        #we modify the the queryset
        form.base_fields['primary_tag'].queryset = obj.tags
        return form
    '''
admin.site.unregister(Tag)
admin.site.register(Tag, NewTagAdmin, inlines=[TagInfoInline])
#    list_editable = ["selector"]







