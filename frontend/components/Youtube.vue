<template>
    <div class="youtube">
        <lite-youtube
            :videoid="id"
            :playlabel="label"
            class="mx-auto"
        />
    </div>
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