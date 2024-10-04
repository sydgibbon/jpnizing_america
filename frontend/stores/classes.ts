type ClassesState = {
    currentVideo: string,
  }
  export const useClassesStore = defineStore('classesStore', {
      state: () => ({
        currentVideo:'wDpsF90DoeI'
      } as ClassesState),
      actions: {
        setVideo(video : string){
            console.log("PASASSSS")
            this.currentVideo = video;
        }
      }
    })
    