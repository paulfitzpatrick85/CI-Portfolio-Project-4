credits

I used the walkthrough 'I think thereforew I blog as a template for my site, using its structure to suits my sites needs and changing the code to get what i needed done'. the following code was taken and unchanged:
in index.html:
{% if is_paginated %}         
    <nav aria-label="Page navigation">
        <ul class="pagination justify-content-center">
            {% if page_obj.has_previous %}
            <li><a href="?page={{ page_obj.previous_page_number }}" class="page-link">&laquo; PREV </a></li>
            {% endif %}
            {% if page_obj.has_next %}
            <li><a href="?page={{ page_obj.next_page_number }}" class="page-link"> NEXT &raquo;</a></li>

            {% endif %}
        </ul>
    </nav>
    {% endif %}