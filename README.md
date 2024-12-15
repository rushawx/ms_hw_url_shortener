``` docker run -d -p 8000:80 -v shorturl_data:/app/data rushawx/shorturl-service:latest```

SHORTURL-сервис:
<li>POST/shorten: Принимает полный URL (JSON: {"url":"..."}) и возвращает короткую ссылку.</li>
<li>GET/{short_id}: Перенаправляет на полный URL, если он существует.</li>
<li>GET/stats/{short_id}: Возвращает JSON с информацией о полном URL.</li>
<li>Данные о сокращенных ссылках (short_id-> full_url) хранятся в SQLite.</li>
<li>Призапуске также автоматически создается таблица.</li>
