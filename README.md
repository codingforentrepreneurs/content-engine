
# Content Engine with Django, Kubernetes, TailwindCSS, Twingate & More

We just released new free course (9hr+) on creating and managing a Content Engine.

But first, what is a content engine? Personally, I think sharing large projects through Google Drive is great until.... you run out of storage. I really do not want to have to "make room" for new content in 2024. 

So what to use? AWS S3. 

S3 technology is one of the best ways to store a LOT of content. But...

Navigating through AWS is a behemoth and can cause a lot of headache or errors or frustration. So what to do?

Build a simple UI that sits on top of AWS leveraging just Python, Django, a little JavaScript, and HTMX. These simple tools will allow us to manage our content in a much easier way. But....

How to share it?

First the project needs to always be running (aka deployed) so our customers/clients can access the content on their own time (e.g. Google Drive). To allow us to make it accessible all the time and primarily focusing on just our code, we use buildpacks and Kubernetes. 

While Kubernetes might sound too complex, Kubernetes is one of the best ways to deploy multiple versions of our app(s) while controlling the exact cost(s) that go into running it (in our case it's about $40/mo). Kubernetes can easily and reliably be scaled up to handle more demand (if it comes). But...

Kubernetes requires containers to run. Maybe you know how to build containers with Docker, may not  -- either way, we will use buildpacks from Google that effectively turn your GitHub repo into a PaaS, a lot like how Heroku works, to build your containers without you ever touching Docker or Dockerfiles (although Docker is awesome).

With a container in hand, Kubernetes can do its job and it does it well. But there's a catch...

We want to keep our app private. Running apps on Kubernetes are private until we make them public. So how to do we share it with others?

Enter Twingate.

Thanks to Twingate, this course exists. Also thanks to Twingate, we can securely share our private running resources with anyone we decide. Just a few simple configurations and we're off to the races. In our case, we'll configure a private Kubernetes Service (ClusterIP type) that forwards to our running containers via Kubernetes Deployments.

With this project, we leverage AWS S3's near-unlimited storage without the complicated navigation of AWS and share a work-in-progress not-yet-secure Django application to anyone we choose to build our Content Engine. Here are a few highlights of the topics we'll cover:

- Django
- Kubernetes
- Twingate
- Python Boto3 for S3 Buckets
- Uploading large files with Django, JavaScript, and Boto3
- HTMX
- TailwindCSS & Flowbite
- Auto-generate Docker Containers
- And so much more.


Each topic is covered in the exact amount of detail needed to make this course happen. The video has a number of chapters so you can skip around to the most interesting bits.

A big thank you to Twingate for partnering with me on this course! Check it out now 👇

- Watch it on Youtube: [https://youtu.be/2TX7Pal5NMc](https://youtu.be/2TX7Pal5NMc)
- Add it, for free, to your CFE library on [https://www.codingforentrepreneurs.com/courses/content-engine/](https://www.codingforentrepreneurs.com/courses/content-engine/)
