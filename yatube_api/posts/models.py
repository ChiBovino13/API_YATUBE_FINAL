from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Group(models.Model):
    """Задает название, описание группы, ссылку в адресной строке"""
    description = models.TextField(verbose_name='Описание группы')
    slug = models.SlugField(unique=True, verbose_name='Адрес')
    title = models.CharField(max_length=200, verbose_name='Название группы')

    def __str__(self):
        return self.title


class Post(models.Model):
    """Задает текст поста, дату публикации, автора и группу"""
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts',
        verbose_name='Автор публикации')
    group = models.ForeignKey(
        Group,
        on_delete=models.SET_NULL,
        related_name='posts',
        blank=True,
        null=True,
        verbose_name='Название группы',
        help_text='Группа, к которой будет относиться пост'
    )
    image = models.ImageField(
        verbose_name='Изображение',
        upload_to='posts/',
        blank=True
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата публикации')
    text = models.TextField(
        verbose_name='Содержание записи',
        help_text='Введите текст поста')

    def __str__(self):
        return self.text


class Comment(models.Model):
    """
    Ссылка на пост и автора комментария,
    текст комментария, дата и время комментария.
    """
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Автор комментария',
        help_text='Автор отображается на сайте'
    )
    created = models.DateTimeField(
        verbose_name='Дата публикации',
        help_text='Дата публикации',
        auto_now_add=True,
        db_index=True)
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField(
        verbose_name='Текст комментария',
        help_text='Обязательное поле, не должно быть пустым'
    )

    def __str__(self):
        return self.text


class Follow(models.Model):
    """Подписка пользователя на автора."""
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='follower',
        verbose_name='Пользователь',
    )
    following = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='following',
        verbose_name='Автор',
    )

    class Meta:
        verbose_name_plural = 'Подписки на авторов'

    def __str__(self):
        return self.text
