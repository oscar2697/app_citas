'use server'

import { ID, Query } from "node-appwrite"
import { BUCKET_ID, DATABASE_ID, databases, ENDPOINT, PATIENT_COLLECTION_ID, PROJECT_ID, storage, users } from "../appwrite.config"
import { parseStringify } from "../utils"
import { InputFile } from 'node-appwrite/file'
import bcrypt from 'bcryptjs';

export const createUser = async (user: CreateUserParams) => {
    try {
        const salt = bcrypt.genSaltSync(10);
        const hashedPassword = bcrypt.hashSync(user.password, salt) 
        const newUser = await users.create(
            ID.unique(),
            user.email,
            user.phone,
            user.name,
            hashedPassword 
        )

        return parseStringify(newUser)
    } catch (error: any) {
            console.log(error)
            if (error && error?.code === 409) {
                const documents = await users.list([
                    Query.equal('email', [user.email])
                ])

                return documents.users[0]
            }
        }
    }

export const getUser = async (userId: string) => {
    try {
        const user = await users.get(userId)

        return parseStringify(user)
    } catch (error) {
        console.log(error)
    }
}

export const getPatient = async (userId: string) => {
    try {
        const patients = await databases.listDocuments(
            DATABASE_ID!,
            PATIENT_COLLECTION_ID!,
            [
                Query.equal('userId', userId)
            ]
        )

        return parseStringify(patients.documents[0])
    } catch (error) {
        console.log(error)
    }
}

export const registerPatient = async ({ identificationDocument, ...patient }: RegisterUserParams) => {
    try {
        let file
        const salt = bcrypt.genSaltSync(10);
        patient.password = bcrypt.hashSync(patient.password, salt) 

        if (identificationDocument) {
            const inputFile = identificationDocument && InputFile.fromBuffer(
                identificationDocument?.get('blobFile') as Blob,
                identificationDocument?.get('fileName') as string
            )

            file = await storage.createFile(BUCKET_ID!, ID.unique(), inputFile)
        }

        const newPatient = await databases.createDocument(
            DATABASE_ID!,
            PATIENT_COLLECTION_ID!,
            ID.unique(),

            {
                identificationDocumentId: file?.$id ? file.$id : null,
                identificationDocumentUrl: file?.$id
                    ? `${ENDPOINT}/storage/buckets/${BUCKET_ID}/files/${file.$id}/view??project=${PROJECT_ID}`
                    : null,
                ...patient,
            }
        )

        return parseStringify(newPatient)
    } catch (error) {
        console.log(error)
    }
}

export const loginUser = async ({ email, password }: { email: string, password: string }) => {
    try {
        const userList = await users.list([
            Query.equal('email', [email])
        ]);
        const user = userList.users[0];

        if (!user.password) {
            throw new Error("Error interno: No se puede autenticar.");
        }

        const salt = bcrypt.genSaltSync(10);
        const hashedPassword = bcrypt.hashSync(password, salt)
        const isPasswordValid = bcrypt.compareSync(password, hashedPassword);

        if (!userList.users || userList.users.length === 0) {
            throw new Error("Usuario no encontrado");
        }

        if (!user.password) {
            throw new Error("Error interno: No se puede autenticar.");
        }

        if (!isPasswordValid) {
            throw new Error("Contraseña incorrecta");
        }

        return parseStringify(user); 
    } catch (error: any) {
        console.error("❌ Error en loginUser:", error.message);
        throw new Error(error.message || "Error al iniciar sesión");
    }
};
