from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return HttpResponse("""
        <html>
            <head>
                <title>Playwright Test Page</title>
            </head>
            <body>
                <h1 id="heading">Hello Playwright</h1>
                
                <button onclick="changeText()" id="btn">
                    Click Me
                </button>

                <p id="message">Initial Text</p>

                <script>
                    function changeText() {
                        document.getElementById("message").innerText = "Button Clicked!";
                    }
                </script>
            </body>
        </html>
    """)