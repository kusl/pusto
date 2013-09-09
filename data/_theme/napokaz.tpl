{% set repo="/s/napokaz/src/"%}
<link rel="stylesheet" href="{{ repo }}napokaz.css" />

<script src="http://code.jquery.com/jquery.js"></script>
<script src="{{ repo }}napokaz.js"></script>
<script>
    $(document).ready(function() {
        $.fn.napokaz.defaults.set({
            frontCount: 10,
            frontThumbsize: '60c',
            picasaIgnore: 'hide'
        });
        $('.napokaz').napokaz();
    });
</script>
<style>
    .napokaz {
        display: inline-block;
        *display: inline;
        *zoom: 1;
        margin: 0 5px;
        margin-bottom: 1em;
        vertical-align: top;
    }
</style>
