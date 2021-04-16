# Twinbase

Twinbase is an open source platform for managing and distributing [digital twin documents](https://doi.org/10.1109/ACCESS.2020.3045856).
It is built on git and can be hosted on free-of-charge GitHub services.
See an example server live at [dtw.dtp.fi](https://dtw.dtp.fi).

Twinbase is at __*initial development*__ phase and backwards incompatible changes are expected frequently.
Update mechanisms are not yet implemented.

Twinbase is hosted by Aalto University where its development was initiated as a result of the experience from multiple digital twin related projects.
Twinbase is used as a tool for building the Digital Twin Web introduced in Section III of [this article](https://doi.org/10.1109/ACCESS.2020.3045856).
Experiences with Twinbase are used to develop further versions of the [digital twin document standard](https://github.com/AaltoIIC/dt-document).

## Using Twinbase

A web interface for each properly configured Twinbase can found from the URL shown on the `baseurl` field in the [/docs/index.yaml](/docs/index.yaml) file.

To fetch the twin documents in python, you can use the [dtweb-python](https://github.com/juusoautiosalo/dtweb-python) library.

## To create your own Twinbase

1. Create a new repository with the "Use this template" button on the [twinbase/twinbase](https://github.com/twinbase/twinbase) page. (Sign in to GitHub if you can't see the button.)
2. In the newly created repository, activate GitHub Actions from the Actions tab if necessary, and manually run the "File modifier" workflow. (This will modify the files to match your GitHub account. Running the workflow several times will not cause any harm.)
3. Activate GitHub Pages from Settings > Pages > Source to `main` branch and `/docs` folder.
4. A link to Twinbase will be shown at the Pages page. If you have not made any domain customizations, it is in the form \<username\>.github.io/\<repository name\>.
5. Unfortunately any updates from the template repository must be made manually. But you can also just make another Twinbase and copy your twin folders and files there.

Forks can be used as well and might make updating easier, but their use has not been properly tested.

### Creating new twins to your Twinbase

Recommended method to create new twins is to use the new-twin page found on the front page of each Twinbase.

After creating a twin, you need to activate its DT identifier with one of these methods: 
   - To activate the automatically generated dtid.org identifier, send the values of dt-id and hosting-iri of each twin to [this form](https://dtid.org/form).
   - Or you can overwrite the dt-id with the URL given by any [URL shortener service](https://en.wikipedia.org/wiki/URL_shortening#Services) or the [perma-id](https://github.com/perma-id/w3id.org) service. The URL needs to redirect to the hosting-iri.

## To start developing Twinbase

Contribution guidelines are not yet established, but useful contributions are welcome! For development, you can try this:
1. Create your own Twinbase using the Template.
2. Modify your Twinbase as you wish in GitHub.
3. Fork [twinbase/twinbase](https://github.com/twinbase/twinbase). (Do not activate Actions to avoid unnecessary commits.)
4. Manually copy the useful modifications from the repository created with the Template.
5. Submit a pull request.

Local development is a bit tricky as Twinbase uses GitHub Actions as an intergal part of the platform, but feel free to try!

## Support

There are currently no official support mechanisms for Twinbase, but [Juuso](https://juu.so) may be able to help.

## Thanks

Twinbase uses [json-view](https://github.com/pgrabovets/json-view) by [pgrabovets](https://github.com/pgrabovets) to display digital twin documents.
Thanks for the nice piece of software!
