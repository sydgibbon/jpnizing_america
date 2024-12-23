<template>
<iframe id="ytplayer" type="text/html" width="100%" height="400px"
    src="http://www.youtube.com/embed/WAqsJpqRGkY?autoplay=1&origin=https://japonizandoamerica.com"
    frameborder="0"/>

</template>
<script>
    export default {
        props: {
            id: String,
            label: String,
        },
        fetchOnServer: false,
    }
</script>