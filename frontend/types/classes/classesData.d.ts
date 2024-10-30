export type classData ={
    title: string
    content?: string,
    video: string,
    selected?: boolean
  }
  export type classesData = {
    name: string,
    classes: classData[],
    open?: boolean
  }