from django.contrib import admin
from .models import Article,Comment
# Register your models here.
class CommentInline(admin.TabularInline):
    model = Comment
    extra =0 #if we want no extra fields on the admin page

class ArticleAdmin(admin.ModelAdmin):
    inlines=[
        CommentInline,
    ]

admin.site.register(Article,ArticleAdmin)
admin.site.register(Comment)

# At this point we could add an additional admin field so we’d see the comment and the article
# on this page. But wouldn’t it be better to just see all Comment models related to a single Article
# model? It turns out we can with a Django admin feature called inlines which displays foreign key
# relationships in a visual way.
# There are two main inline views used: TabularInline159 and StackedInline160. The only difference
# between the two is the template for displaying information. In a TabularInline all model fields
# appear on one line while in a StackedInline each field has its own line. We’ll implement both so
# you can decide which one you prefer.
# Update articles/admin.py as follows in your text editor to add the StackedInline view.