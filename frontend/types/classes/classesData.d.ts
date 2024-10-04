export type classData ={
    title: String
    content: String,
    video?: String,
    selected?: boolean
  }
  export type classesData = {
    name: String,
    classes: classData[],
    open?: boolean
  }