package main

import "fmt"
import "net/http"

func index(w http.ResponseWriter, r *http.Request) {
    fmt.Fprintln(w, "Serverless Haxors with golang")
}

func main() {
    http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
        fmt.Fprintln(w, "Serverless Haxors with golang")
    })

    http.HandleFunc("/index", index)

    fmt.Println("starting web server at http://localhost:3510/")
    http.ListenAndServe(":3510", nil)
}
